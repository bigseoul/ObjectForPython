from datetime import datetime, time, timedelta
from recurring_schedule_ import RecurringSchedule
import contracts

class Event:
    def __init__(self, subject, start_time: "datetime", duration: "time") -> None:
        self.__subject = subject
        self.__start_time = start_time
        self.__duration = duration

    def is_satisfied(self, schedule: "RecurringSchedule") -> bool:
        if (
            self.__start_time.weekday() != schedule.day_of_week
            or self.__start_time.time() != schedule.start_time
            or self.__duration != schedule.duration
        ):
            return False
        return True

    def reschedule(self, schedule: "RecurringSchedule") -> None:
        
        
        self.__start_time = self.__start_time + timedelta(
            days=self.__days_distance(schedule)
        )
        self.__duration = schedule.duration
        print("Event's been rescheduled.")
        print("start_time: ", self.__start_time)
        print("duration: ", self.__duration)

    def __days_distance(self, schedule: "RecurringSchedule") -> int:
        return schedule.day_of_week - self.__start_time.weekday()
