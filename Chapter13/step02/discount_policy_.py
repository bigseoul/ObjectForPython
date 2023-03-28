from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from money_ import Money
from datetime import datetime

if TYPE_CHECKING:
    from screening_ import Screening
    from discount_condition_ import AbsDiscountCondition

    # 아니 PeriodCondition도 받겠지.. 그러면 타입 힌트에 이거 쓰면 안되겠네


class AbsDiscountPolicy(metaclass=ABCMeta):
    def __init__(self, *args: "AbsDiscountCondition") -> None:
        self.__conditions = list(args)

    def calculate_discount_amount(self, screening: "Screening"):
        # 사전조건
        self._check_precondition(screening)

        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                amount = self.get_discount_amount(screening)
                self._check_postcondition(amount)  # type: ignore
                return self.get_discount_amount(screening)

        # NonDiscoutPolicy, condition이 없는 경우
        # return Money.wons(0) 해도 됨.
        return self.get_discount_amount(screening)

    def _check_precondition(self, screening: "Screening"):
        assert screening != None and screening.get_start_time() > datetime.now()

    def _check_postcondition(self, amount: Money):
        assert amount != None and amount.is_greater_than_or_equal(Money.wons(0))

    @abstractmethod
    def get_discount_amount(self, screening: "Screening"):
        pass
