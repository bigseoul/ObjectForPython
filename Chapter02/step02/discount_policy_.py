from abc import *
from typing import TYPE_CHECKING
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening
    from discount_condition_ import AbsDiscountCondition

    # 아니 PeriodCondition도 받겠지.. 그러면 타입 힌트에 이거 쓰면 안되겠네

""" PeriodCondition과 SequenceCondition의 타입 힌트를 위해
    AbsDiscountCondition을 써도 되나? 
    머 타입힌트고 스태틱메서드 하나만 있으니까.. 괜춚?
"""


class AbsDiscountPolicy(metaclass=ABCMeta):
    # discountPolicy는 discountCondition 인자 여러 개를 가질 수 있다.
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        self.__conditions = list(args)

    """NoneDisdountPolicy는 호출이 안되네?
        condition이 없는 경우가 있는데 이를 생각지 않고
        끝라인에 retrun Money.wons(0)을 안쳐넣었음.
        그런데 말입니다.. nondiscountdisp 가서 고민 참고"""

    def calculate_discount_amount(self, screening: "Screening"):

        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                return self.get_discount_amount(screening)

        # NonDiscoutPolicy, condition이 없는 경우
        # return Money.wons(0) 해도 됨.
        return self.get_discount_amount(screening)

    @abstractmethod
    def get_discount_amount(self, screening: "Screening"):
        pass
