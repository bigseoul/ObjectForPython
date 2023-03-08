from abc import ABCMeta, abstractmethod

from discount_condition_ import AbsDiscountCondition
from discount_policy_ import AbsDiscountPolicy
from money_ import Money
from screening_ import Screening


class DefaultDiscountPolicy(AbsDiscountPolicy, metaclass=ABCMeta):
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        """
        DefaultDiscountPolicy는 discountCondition 인자 여러 개를 가질 수 있다.
        """
        self.__conditions = list(args)

    def __str__(self) -> str:
        return f"할인조건: {self.__conditions}"

    # override
    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        """4. 할인조건에게 상영될 영화의 조건이 할인조건에 맞는지 물어보는 메시지 전달"""
        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                # 4-1. 조건이 맞는다면, 내부 구현,(AmountDiscountPolicy, Percent~)에게 할인정도 계산해달라고 메시지 전달
                return self._get_discount_amount(screening)

        return Money.from_wons(0)  # NoneDisdountPolicy 의 경우

    @abstractmethod
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        pass
