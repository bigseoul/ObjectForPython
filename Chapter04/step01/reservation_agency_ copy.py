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
        self, screening: "Screening", customer: "Customer", audience_count
    ) -> Reservation:
        movie: "Movie" = screening.movie
        discountable = self.is_discountable(movie, screening)

        fee: "Money" = self.calculate_fee(movie, discountable, audience_count)

        return Reservation(customer, screening, fee, audience_count)

    def is_discountable(self, movie: "Movie", screening: "Screening") -> bool:
        for condition in movie.discount_conditions:
            if condition.type == DiscountConditionType.PERIOD:
                discountable = (
                    condition.day_of_week == screening.when_screened.weekday()
                    and condition.start_time.time() <= screening.when_screened.time()
                    and condition.end_time.time() >= screening.when_screened.time()
                )
            else:
                discountable = condition.sequence == screening.sequence

            if discountable:
                return True

        return False

    def calculate_fee(
        self, movie: "Movie", discountable: bool, audience_count: int
    ) -> "Money":
        if discountable:
            discount_amount: "Money" = self.get_discount_amount(movie)
            minus_fee: "Money" = movie.fee
            fee = minus_fee.minus(discount_amount).times(audience_count)
        else:
            fee = movie.fee.times(audience_count)

        return fee

    def get_discount_amount(self, movie: "Movie") -> "Money":
        if movie.movie_type == MovieType.AMOUNT_DISCOUNT:
            return movie.discount_amount
        elif movie.movie_type == MovieType.PERCENT_DISCOUNT:
            temp_fee: "Money" = movie.fee
            return temp_fee.times(movie.discount_percent)
        else:
            return Money.from_wons(0)
