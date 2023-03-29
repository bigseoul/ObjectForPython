from date_time_interval_ import DateTimeInterval
from day_of_weeks_ import DAY_OF_WEEK
from datetime import timedelta
from money_ import Money


class DayOfWeekDiscountRule:
    def __init__(self, day_of_weeks, duration: timedelta, amount: Money) -> None:
        self.__day_of_weeks = day_of_weeks
        self.__duration = duration
        self.__amount = amount

    # override
    def calculate(self, interval: DateTimeInterval):
        "전화한 요일(interval)이 요일별 할인 규칙(day_of_weeks) 안에 있으면, 요금 계산해서 리턴"
        if interval.from_time.weekday() in self.__day_of_weeks:
            return self.__amount.times(
                interval.duration().total_seconds() / self.__duration.total_seconds()
            )
        return Money.wons(0)
