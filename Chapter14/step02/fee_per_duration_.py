from math import ceil
from money_ import Money
from datetime import timedelta
from date_time_interval_ import DateTimeInterval


class FeePerDuration:
    def __init__(self, fee: Money, duration: timedelta) -> None:

        self.__fee = fee  # 단위요금
        self.__duration = duration  # 단위시간

    def calculate(self, interval: DateTimeInterval) -> Money:
        """단위 시간당 요금, 일정 기간 동안의 요금 계산"""
        interval_duration = interval.duration().total_seconds()
        duration = self.__duration.total_seconds()
        return self.__fee.times(ceil(interval_duration / duration))
