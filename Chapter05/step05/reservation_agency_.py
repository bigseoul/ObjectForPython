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
        ...
        # 1. 할인여부 체크
        discountable = self.check_discountable(screening)
        # 2. 요금계산
        fee = self.calcualte_fee(screening, discountable, audience_count)
        # 3. 예약하기
        return self.create_reserve(customer, screening, fee, audience_count)

    def check_discountable(self, screening: "Screening"):
        return any(
            self.is_discountable(condition, screening)
            for condition in screening.movie.discount_conditions
        )

    def is_discountable(
        self, condition: "DiscountCondition", screening: "Screening"
    ) -> bool:
        if condition.type == DiscountConditionType.PERIOD:
            return self.is_safisfied_by_period(condition, screening)
        elif condition.type == DiscountConditionType.SEQUENCE:
            return self.is_safisfied_by_sequence(condition, screening)
        return False

    def is_safisfied_by_period(
        self, condition: "DiscountCondition", screening: "Screening"
    ) -> bool:
        if condition.start_time and condition.end_time:
            current_weekday = screening.when_screened.weekday()
            current_time = screening.when_screened.time()

            return (
                condition.day_of_week == current_weekday
                and condition.start_time.time() <= current_time
                and condition.end_time.time() >= current_time
            )
        return False

    def is_safisfied_by_sequence(
        self, condition: "DiscountCondition", screening: "Screening"
    ):
        return condition.sequence == screening.sequence

    def calcualte_fee(
        self, screeing: "Screening", discountable: bool, audience_count: int
    ) -> Money:
        if discountable:
            return screeing.movie.fee.minus(
                self.calculate_discounted_fee(screeing.movie)
            ).times(audience_count)
        return screeing.movie.fee

    def calculate_discounted_fee(self, movie: "Movie") -> Money:
        """영화가격에서 할인율 계산"""
        if movie.movie_type == MovieType.AMOUNT_DISCOUNT:
            return self.calculate_amount_discounted_fee(movie)
        elif movie.movie_type == MovieType.PERCENT_DISCOUNT:
            return self.calculate_percent_discounted_fee(movie)
        elif movie.movie_type == MovieType.NONE_DISCOUNT:
            return self.calculate_none_discounted_fee(movie)
        return Money.from_wons(0)

    def create_reserve(self, customer, screening, fee, audience_count):
        return Reservation(customer, screening, fee, audience_count)

    def calculate_amount_discounted_fee(self, movie: "Movie") -> Money:
        return movie.discount_amount

    def calculate_percent_discounted_fee(self, movie: "Movie") -> Money:
        return movie.fee.times(movie.discount_percent)

    def calculate_none_discounted_fee(self, movie: "Movie") -> Money:
        return Money.from_wons(0)  # get_fee?
