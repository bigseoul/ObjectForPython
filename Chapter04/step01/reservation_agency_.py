from typing import TYPE_CHECKING

from discount_condition_type_ import DiscountConditionType
from money_ import Money
from movie_type_ import MovieType
from reservation_ import Reservation

if TYPE_CHECKING:
    from customer_ import Customer
    from discount_condition_ import DiscountCondition
    from movie_ import Movie
    from screening_ import Screening


class ReservationAgency:
    def reserve(
        self, screening: "Screening", customer: "Customer", audience_count: int
    ) -> Reservation:
        if screening.movie is None:  # 1 of 4: screeing에 의존
            raise ValueError("Screening movie is None")
        else:
            movie: "Movie" = screening.movie  # 2 of 4: movie 의존
        """
        할인 가능 여부 체크
        P182) 디미터의 법칙 위반 
        """
        discountable = False

        # Discountcondition에 대해 루프를 돌면서 할인 가능 여부를 확인한다. discountable 변수의 값을 체크하고 적절한 할인 정책에 따라 예매 요금을 계산한다.
        for condition in movie.discount_conditions:  # 3 of 4: condition 의존
            condition: "DiscountCondition" = condition
            if condition.type == DiscountConditionType.PERIOD:
                # when_screened 게터에 리턴 타입 힌트 줌.
                if condition.start_time is not None and condition.end_time is not None:
                    discountable = (
                        condition.day_of_week == screening.when_screened.weekday()
                        and condition.start_time.time()
                        <= screening.when_screened.time()
                        and condition.end_time.time() >= screening.when_screened.time()
                    )
            else:
                discountable = condition.sequence == screening.sequence

            if discountable:
                break

        # discountable 변수의 값을 체크하고 적절한 할인 정책에 따라 예매 요금을 계산하는 if문.
        fee: "Money" = Money.from_wons(0)
        if discountable:  # true이면
            discount_amount: "Money" = Money.from_wons(0)
            # 문제,낮은 응집도)할인정책을 판단하는 코드와 할인 정책을 선택하는 코드가 함께 있음.
            if movie.movie_type == MovieType.AMOUNT_DISCOUNT:
                discount_amount = movie.discount_amount
            elif movie.movie_type == MovieType.PERCENT_DISCOUNT:
                temp_fee: "Money" = movie.fee
                discount_amount = temp_fee.times(movie.discount_percent)
            elif movie.movie_type == MovieType.NONE_DISCOUNT:
                discount_amount = Money.from_wons(0)
            """
            문제)높은 결합도
            -객체 내부 구현이 외부인터페이스에 드러난다는 것은 클라이언트가 구현에 강하게 결합된 것
            -객체 내부 구현 변경시, 이 인터페이스에 의존하는 모든 클라이언트 모두 변경해야 해
            -fee의 타입(데이터/메서드)을 변경한다면, ReservationAgency도 같이 변경해야 해.
            -'getFee():여기선 movie.fee'는 fee를 정상적으로 캡슐화 못함. 
            -또한 이를 사용하는 것은 인스턴스 변수 fee의 가시성을 private에서 public으로 변경하는 것. 
            -(이를 통해 fee인스턴스를 리턴받으니까... ) *덜이해됨
            
            -여러 데이터 객체들을 쓰는 제어로직이 특정 객체 안에 집중되기에 
            제어 객체 하나가 여러 데이터 객체에 강하게 결합된다. 
            -결국 어떤 데이터 객체가 변경되면 제어 객체도 변경해야 됨.
            
            -제어 객체인 ReservationAgency가 모든 데이터 객체에 의존함.  
            """
            fee: "Money" = movie.fee
            fee = fee.minus(discount_amount).times(audience_count)
        else:
            fee: "Money" = movie.fee  # type: ignore
            fee = fee.times(audience_count)

        return Reservation(
            customer, screening, fee, audience_count
        )  # 4 of 4: Reservation 의존
