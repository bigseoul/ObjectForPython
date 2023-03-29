from fee_condition_ import FeeCondition
from date_time_interval_ import DateTimeInterval
from call_ import Call
from day_of_weeks_ import DAY_OF_WEEK


class DayOfWeekFeeCondition(FeeCondition):
    def __init__(self, *day_of_weeks) -> None:
        self.__day_of_weeks = list(day_of_weeks)

    # override
    def find_time_interval(self, call: Call) -> list[DateTimeInterval]:

        # intervals = call.get_interval().split_by_day()
        # return [each for each in intervals if each.from_time.weekday() in self.__day_of_weeks]
        intervals = []
        for interval in call.get_interval().split_by_day():
            if interval.from_time.weekday() in self.__day_of_weeks:
                intervals.append(interval)
        return intervals
