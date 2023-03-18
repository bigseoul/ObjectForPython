from typing import TYPE_CHECKING
from discount_condition_type_ import DiscountConditionType
from money_zero import MoneyZero

from reservation_ import Reservation
from money_ import Money
from movie_type_ import MovieType

if TYPE_CHECKING:
    from screening_ import Screening
    from customer_ import Customer
    from movie_ import Movie
    from discount_condition_ import DiscountCondition


class ReservationAgency:
    # return type이 Reservation임.
    def reserve(
        screening: "Screening", customer: "Customer", audience_count
    ) -> Reservation:
        movie: "Movie" = screening.movie

        """할인 가능 여부 체크"""
        discountable = False

        """checkDiscountable()로 분리"""
        # condition에 타입힌트 DiscountCondition를 어떻게 주지? 안에서 재할당 ㅋ
        for condition in movie.discount_conditions:
            condition: "DiscountCondition" = condition
            if condition.type == DiscountConditionType.PERIOD:

                # when_screened 게터에 리턴 타입 힌트 줌.
                discountable = (
                    condition.day_of_week == screening.when_screened.weekday()
                    and condition.start_time.time() <= screening.when_screened.time()
                    and condition.end_time.time() >= screening.when_screened.time()
                )
                print("discountable:", discountable)
            else:
                discountable = condition.sequence == screening.sequence

            if discountable:
                print("Yes, it's discountable. break")
                break

        fee: "Money" = None
        if discountable:
            print("apply discount")
            discount_amount: "Money" = MoneyZero.ZERO
            #문제,낮은 응집도)할인정책을 판단하는 코드와 할인 정책을 선택하는 코드가 함께 있음.
            if movie.movie_type == MovieType.AMOUNT_DISCOUNT:
                discount_amount = movie.discount_amount
            elif movie.movie_type == MovieType.PERCENT_DISCOUNT:
                temp_fee: "Money" = movie.fee
                discount_amount = temp_fee.times(movie.discount_percent)
            elif movie.movie_type == MovieType.NONE_DISCOUNT:
                discount_amount = MoneyZero.ZERO
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
            minus_fee: "Money" = movie.fee
            
            # 같은 객체니까... 마이너스로 머니를 리턴했으니, 다시 타임스 접근 가능하지 ㅋ;
            fee = minus_fee.minus(discount_amount).times(audience_count)
        else:
            else_fee: "Money" = movie.fee  # type: ignore
            fee = else_fee.minus(discount_amount)

        return Reservation(customer, screening, fee, audience_count)
