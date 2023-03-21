from datetime import time
from typing import TYPE_CHECKING

from money_ import Money
from movie_ import AbsMovie

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition


class PercentDiscountMovie(AbsMovie):
    def __init__(
        self,
        title: str,
        running_time: time,
        fee: Money,
        percent: float,
        *discount_conditions: "AbsDiscountCondition"
    ) -> None:
        super().__init__(title, running_time, fee, *discount_conditions)
        self.__percent = percent

    def _calculate_discount_amount(self):
        return self._getFee() * self.__percent  # movie의 getFee()
