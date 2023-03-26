from datetime import time
from typing import TYPE_CHECKING, List
from money_zero import MoneyZero
from call_ import Call
from money_ import Money

if TYPE_CHECKING:
    ...


class NightlyDiscountPhone:

    LATE_NIGHT_HOUR: int = 22

    def __init__(
        self, nightly_amount: "Money", regular_amount: "Money", seconds: "time"
    ) -> None:
        self.__nightly_amount = nightly_amount
        self.__regular_amount = regular_amount
        self.__seconds = seconds
        self.__calls = []

    def call(self, call: Call) -> None:
        self.__calls.append(call)

    def get_calls(self) -> List:
        return self.__calls

    def get_nightly_amount(self) -> Money:
        return self.__nightly_amount

    def get_regular_amount(self) -> Money:
        return self.__regular_amount

    def get_seconds(self) -> time:
        return self.__seconds

    def calculate_fee(self) -> Money:  # type: ignore
        result = MoneyZero.ZERO
        call: "Call" = None  # type: ignore
        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )

        """통화시작 시간 기준. """
        for call in self.__calls:
            if call.start_time.hour >= NightlyDiscountPhone.LATE_NIGHT_HOUR:
                result = result.plus(
                    self.__nightly_amount.times(call.get_duration() / (unit_time))
                )
            else:
                result = result.plus(
                    self.__regular_amount.times(call.get_duration() / (unit_time))
                )
            return result
