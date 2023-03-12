from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening
    from customer_ import Customer
    from discount_condition_ import DiscountCondition
    from money_ import Money


class Reservation:
    def __init__(self, customer: "Customer", screening: "Screening", fee: "Money", audience_count) -> None:
        self.customer = customer
        self.screening = screening
        self.fee = fee
        self.audience_count = audience_count
