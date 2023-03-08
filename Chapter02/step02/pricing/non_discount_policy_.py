import logging
from typing import TYPE_CHECKING

from discount_policy_ import AbsDiscountPolicy
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening


class NonDiscountPolicy(AbsDiscountPolicy):
    # override
    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        return Money.from_wons(0)
