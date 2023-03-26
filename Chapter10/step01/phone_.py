from datetime import time
from typing import TYPE_CHECKING, List
from money_zero import MoneyZero
from call_ import Call
from money_ import Money

if TYPE_CHECKING:
    ...


class Phone:
    def __init__(self, amount: Money, seconds: time) -> None:
        self.__amount = amount
        self.__seconds = seconds
        self.__calls = []

    def call(self, call: Call) -> None:
        self.__calls.append(call)

    def get_calls(self) -> List:
        return self.__calls

    def get_amount(self) -> Money:
        return self.__amount

    def get_seconds(self) -> time:
        return self.__seconds

    def calculate_fee(self) -> Money:
        result = MoneyZero.ZERO
        call: Call = None  # type: ignore

        """python은 자바의 Duration.getSeconds()같이 초로 환산해서 리턴해주는 게 없음"""
        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )

        for call in self.__calls:
            result = result.plus(self.__amount.times(call.get_duration() / (unit_time)))
        return result
