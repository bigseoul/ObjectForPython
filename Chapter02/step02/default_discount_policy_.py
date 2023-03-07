from abc import ABCMeta, abstractmethod

from discount_condition_ import AbsDiscountCondition
from discount_policy_ import AbsDiscountPolicy
from money_ import Money
from screening_ import Screening


class DefaultDiscountPolicy(AbsDiscountPolicy, metaclass=ABCMeta):
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        """
        discountPolicy는 discountCondition 인자 여러 개를 가질 수 있다.
        """
        self.__conditions = list(args)

    def __str__(self) -> str:
        return f"할인정책: {self.__conditions}"

    # override
    def calculate_discount_amount(self, screening: "Screening") -> "Money":

        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                return self._get_discount_amount(screening)

        return Money.from_wons(0)  # NoneDisdountPolicy 의 경우

    @abstractmethod
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        pass
