from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, List
from money_zero import MoneyZero
from call_ import Call
from money_ import Money
from phone_ import Phone


class Phone(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__calls = []

    def call(self, call):
        self.__calls.append(call)

    def get_calls(self) -> List:
        return self.__calls

    def after_calculated(self, fee: Money) -> Money:
        return fee

    """전체 통화 목록 통화요금 계산"""

    def calculate_fee(self) -> Money:
        result = MoneyZero.ZERO

        for call in self.__calls:
            result = result.plus(self._calculate_call_fee(call))
        return result

    """자식 클래스에서 오버라이딩 할 수 있도록 protected로 선언"""

    @abstractmethod
    def _calculate_call_fee(self, call: Call) -> Money:
        ...
