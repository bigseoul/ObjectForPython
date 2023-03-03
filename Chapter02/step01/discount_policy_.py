from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    from screening_ import Screening


class AbsDiscountPolicy(metaclass=ABCMeta):
    # discountPolicy는 discountCondition 인자 여러 개를 가질 수 있다.
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        self.__conditions = list(args)

    """NoneDisdountPolicy는 호출이 안되네?
        condition이 없는 경우가 있는데 이를 생각지 않고
        끝라인에 retrun Money.wons(0)을 안쳐넣었음.
        그런데 말입니다.. nondiscountdisp 가서 고민 참고"""

    def __str__(self) -> str:
        return f"할인정책: {self.__conditions}"

    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                return self.get_discount_amount(screening)

        # condition이 없는 경우
        # return Money.wons(0) 해도 됨.
        return self.get_discount_amount(screening)

    # if self.__conditions == None:
    #     return self.get_discount_amount(screening)
    # else:
    #     for condition in self.__conditions:
    #         if condition.is_satisfied_by(screening):
    #             return self.get_discount_amount(screening)

    #  for condition in self.__conditions:
    #     if condition.is_satisfied_by(screening):
    #         return self.get_discount_amount(screening)

    # if self.__conditions is True:
    #     for condition in self.__conditions:
    #         if condition.is_satisfied_by(screening):
    #             return self.get_discount_amount(screening)

    @abstractmethod
    def get_discount_amount(self, screening: "Screening") -> "Money":
        pass
