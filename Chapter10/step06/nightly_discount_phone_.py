from datetime import time
from typing import TYPE_CHECKING

from abtract_phone_ import AbstractPhone
from call_ import Call
from money_ import Money


class NightlyDiscountPhone(AbstractPhone):

    LATE_NIGHT_HOUR: int = 22

    def __init__(
        self, nightly_amount: Money, regular_amount: Money, seconds: time
    ) -> None:
        self.__nightly_amount = nightly_amount
        self.__regular_amount = regular_amount
        self.__seconds = seconds
        super().__init__()

    # Override
    def _calculate_call_fee(self, call: Call) -> Money:

        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )

        if call.start_time.hour >= NightlyDiscountPhone.LATE_NIGHT_HOUR:
            return self.__nightly_amount.times(call.get_duration() / (unit_time))
        else:
            return self.__regular_amount.times(call.get_duration() / (unit_time))
