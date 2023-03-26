class RecurringSchedule:
    def __init__(self, subject, day_of_week, start_time, duration) -> None:
        self.__subject = subject
        self.__day_of_week = day_of_week
        self.__start_time = start_time
        self.__duration = duration

    @property
    def day_of_week(self):
        return self.__day_of_week

    @property
    def start_time(self):
        return self.__start_time

    @property
    def duration(self):
        return self.__duration
