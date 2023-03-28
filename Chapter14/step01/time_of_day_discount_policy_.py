import logging
from basic_rate_policy_ import BasicRatePolicy
from money_ import Money
from datetime import datetime, timedelta, time, date
from call_ import Call
from date_time_interval_ import DateTimeInterval


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    ...


class TimeOfDayDiscountPolicy(BasicRatePolicy):
    """
    시간대별로 분할하는 작업 전문가
    """

    def __init__(self, starts, ends, duration, amount) -> None:
        self.__starts: list[time] = starts  # 시작시작 0시
        self.__ends: list[time] = ends  # 종료시간 19시
        self.__duration: list[timedelta] = duration  # 단위시간 10초
        self.__amount: list[Money] = amount  # 단위요금 18원

    # override
    def _calculate_call_fee(self, call: Call) -> Money:
        result = Money.wons(10)
        for interval in call.split_by_day():
            for loop in range(len(self.__starts)):
                result = result.plus(
                    self.__amount[loop].times(
                        (
                            datetime.combine(
                                date.today(), self.__to(interval, self.__ends[loop])
                            )
                            - datetime.combine(
                                date.today(), self.__from(interval, self.__starts[loop])
                            )
                        ).total_seconds()
                        / self.__duration[loop].total_seconds()
                    )
                )
        return result

    def __from(self, interval: DateTimeInterval, from_time: time) -> time:
        return (
            from_time
            if interval.from_time.time() < from_time
            else interval.from_time.time()
        )

    def __to(self, interval: DateTimeInterval, to_time: time) -> time:
        return to_time if interval.to_time.time() > to_time else interval.to_time.time()
