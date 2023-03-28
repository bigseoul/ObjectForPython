from datetime import datetime, date, time, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from date_time_interval_ import DateTimeInterval


class DateTimeInterval:
    """기간 자체를 처리하는 전문가"""

    def __init__(self, from_time: datetime, to_time: datetime) -> None:
        self.__from_time = from_time
        self.__to_time = to_time

    """정적 팩토리 메서드"""

    @classmethod
    def from_combine(cls, from_time, to_time):
        return cls(from_time, to_time)

    @classmethod
    def from_to_midnight(cls, from_time: datetime):
        return cls(
            from_time, datetime.combine(from_time.date(), time(23, 59, 59, 999999))
        )

    @classmethod
    def from_from_midnight(cls, to_time: datetime):
        return cls(datetime.combine(to_time.date(), time(0, 0)), to_time)

    @classmethod
    def from_during(cls, date: date):
        return cls(
            datetime.combine(date, time(0, 0)),
            datetime.combine(date, time(23, 59, 59, 999999)),
        )

    def duration(self) -> timedelta:
        return self.__to_time - self.__from_time

    @property
    def from_time(self):
        return self.__from_time

    @property
    def to_time(self):
        return self.__to_time

    def split_by_day(self) -> list["DateTimeInterval"]:

        if self.days() > 0:
            return self.__split(self.days())

        return [self]

    def days(self) -> int:
        return self.__to_time.day - self.__from_time.day

    def __split(self, days: int) -> list["DateTimeInterval"]:
        result: list["DateTimeInterval"] = []
        self.add_first_day(result)
        self.add_middle_days(result, days)
        self.add_last_day(result)
        return result

    def add_first_day(self, result: list["DateTimeInterval"]) -> None:
        result.append(DateTimeInterval.from_to_midnight(self.__from_time))

    def add_middle_days(self, result: list["DateTimeInterval"], days):
        for loop in range(1, days):
            result.append(
                DateTimeInterval.from_during(
                    (self.__from_time + timedelta(days=loop)).date()
                )
            )

    def add_last_day(self, result: list["DateTimeInterval"]) -> None:
        result.append(DateTimeInterval.from_from_midnight(self.__to_time))
