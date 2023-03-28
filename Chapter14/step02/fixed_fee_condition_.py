from fee_condition_ import FeeCondition
from date_time_interval_ import DateTimeInterval
from call_ import Call


class FixedFeeCondition(FeeCondition):

    # override
    def find_time_interval(self, call: Call) -> list[DateTimeInterval]:
        return [call.get_interval()]

