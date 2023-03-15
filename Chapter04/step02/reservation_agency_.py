from typing import TYPE_CHECKING, Optional

from money_ import Money
from reservation_ import Reservation

if TYPE_CHECKING:
    from customer_ import Customer
    from discount_condition_ import DiscountCondition
    from movie_ import Movie
    from screening_ import Screening


class ReservationAgency:
    """
    A class that represents a reservation agency that can reserve screenings for customers.
    """

    def reserve(
        self, screening: "Screening", customer: "Customer", audience_count: int
    ) -> "Reservation":
        fee: Optional[Money] = screening.calculate_fee(audience_count)
        return Reservation(customer, screening, fee, audience_count)
