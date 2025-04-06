from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from call_ import Call
from rate_policy_ import RatePolicy
from money_ import Money
from money_zero import MoneyZero

if TYPE_CHECKING:
    from phone_ import Phone


class BasicRatePolicy(RatePolicy, metaclass=ABCMeta):
    # Override

    def calculate_fee(self, phone: "Phone") -> Money:
        """
        상속과 관계 없는 Phone을 받음
        RegularPolicy가 Phone에 주입되었기 때문.
        """
        result = MoneyZero.ZERO

        for call in phone.get_calls():
            result = result.plus(self._calculate_call_fee(call))

        return result

    @abstractmethod
    def _calculate_call_fee(self, call: Call) -> Money:
        ...
