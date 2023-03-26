from datetime import datetime, time, timedelta
from recurring_schedule_ import RecurringSchedule

class Event:
    def __init__(self, subject, start_time: "datetime", duration: "time") -> None:
        self.__subject = subject
        self.__start_time = start_time
        self.__duration = duration

    def is_satisfied(self, schedule: "RecurringSchedule"):
        if (
            self.__start_time.weekday() != schedule.day_of_week
            or self.__start_time.time() != schedule.start_time
            or self.__duration != schedule.duration
        ):

            """
            1. 스캐줄에 맞게 이벤트를 수정
            2. 수정했으니 True이나 False를 반환
            3. 다음 조회에서는 여기로 들어오지 않고 True가 반함됨.
            4. is_satisfiedr가 명령과 쿼리 두가지 역할을 동시에 함.
            """
            self.__reschedule(schedule)
            print("false")
            return False

        print("True")
        return True

    def __reschedule(self, schedule: "RecurringSchedule") -> None:
        self.__start_time = self.__start_time + timedelta(
            days=self.__days_distance(schedule)
        )
        self.__duration = schedule.duration

    def __days_distance(self, schedule: "RecurringSchedule") -> int:
        return schedule.day_of_week - self.__start_time.weekday()
