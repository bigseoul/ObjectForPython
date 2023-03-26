from datetime import datetime, time


class Call:
    def __init__(self, start_time: datetime, end_time: datetime) -> None:
        self.__start_time = start_time
        self.__end_time = end_time

    def get_duration(self):
        result = self.__end_time - self.__start_time

        return result.total_seconds()

    @property
    def start_time(self) -> datetime:
        return self.__start_time
