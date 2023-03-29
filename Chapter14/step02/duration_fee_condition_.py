from datetime import timedelta, datetime
from fee_condition_ import FeeCondition
from date_time_interval_ import DateTimeInterval
from call_ import Call


class DurationFeeCondition(FeeCondition):
    """
    구간별 방식 : 전체 통화시간을 일정한 통화시간에 따라 나누고 구간별로 요금을 차등부과
    형식: 초기 A분 동안 B초당 C원; A분 ~ D분까지 B초당 D원; D분 초과시 B초당 E원
    예: 초기 1분동안 10초당 50원, 초기 1분 이후 10초당 20원

    """

    def __init__(self, from_time: timedelta, to_time: timedelta) -> None:
        self.__from_time = from_time
        self.__to_time = to_time

    # override
    def find_time_interval(self, call: Call) -> list[DateTimeInterval]:
        if call.get_duration() < self.__from_time:
            return []

        return [
            (
                DateTimeInterval.from_combine(
                    (call.get_from() + self.__from_time),
                    (call.get_from() + self.__to_time)
                    if call.get_duration() > self.__to_time
                    else call.get_to(),
                )
            )
        ]
