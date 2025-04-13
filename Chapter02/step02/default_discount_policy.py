from abc import ABCMeta, abstractmethod
from typing import List

from discount_condition_ import AbsDiscountCondition
from discount_policy_ import AbsDiscountPolicy
from money_ import Money
from screening_ import Screening


class DefaultDiscountPolicy(AbsDiscountPolicy, metaclass=ABCMeta):
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        self.__conditions = list(args)

    def __str__(self) -> str:
        return f"Discount Conditions: {self.__conditions}"

    # overrided
    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                return self._get_discount_amount(screening)

        return Money.from_wons(0)

    @abstractmethod
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        pass
