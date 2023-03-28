from datetime import datetime, time, timedelta
from date_time_interval_ import DateTimeInterval


class Call:
    """1. 통화 기간을 일자 단위로 나누는 전문가"""

    def __init__(self, from_time: datetime, to_time: datetime) -> None:
        self.__interval = DateTimeInterval.from_combine(from_time, to_time)

    def get_duration(self) -> timedelta:
        return self.__interval.duration()

    def get_from(self):
        return self.__interval.from_time

    def get_to(self):
        return self.__interval.to_time

    def get_interval(self):
        return self.__interval

    def split_by_day(self) -> list[DateTimeInterval]:
        return self.__interval.split_by_day()
