from datetime import time
from typing import TYPE_CHECKING

from money_ import Money
from movie_ import AbsMovie

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition


class AmountDiscountMovie(AbsMovie):
    def __init__(
        self,
        title: str,
        running_time: time,
        fee: Money,
        discount_amount: Money,
        *discount_conditions: "AbsDiscountCondition"
    ) -> None:
        super().__init__(title, running_time, fee, *discount_conditions)
        self._discount_amount = discount_amount

    def _calculate_discount_amount(self) -> Money:
        return self._discount_amount
