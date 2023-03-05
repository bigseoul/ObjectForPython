from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from .money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    from screening_ import Screening


class AbsDiscountPolicy(metaclass=ABCMeta):
    @abstractmethod
    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        pass
