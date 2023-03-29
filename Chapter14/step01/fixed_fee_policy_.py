from money_ import Money
from call_ import Call
from datetime import time
from basic_rate_policy_ import BasicRatePolicy


class FixedFeePolicy(BasicRatePolicy):
    def __init__(self, amount: Money, seconds: time) -> None:
        self.__amount = amount
        self.__seconds = seconds

    # override
    def _calculate_call_fee(self, call: Call) -> Money:
        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )
        return self.__amount.times(call.get_duration().total_seconds() / unit_time)
