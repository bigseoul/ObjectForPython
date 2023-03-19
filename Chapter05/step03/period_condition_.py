from datetime import time
from typing import TYPE_CHECKING

from discount_condition_ import AbsDiscountCondition

if TYPE_CHECKING:
    from screening_ import Screening


class PeriodCondition(AbsDiscountCondition):
    def __init__(self, day_of_week: int, start_time: time, end_time: time) -> None:
        self.__day_of_week = day_of_week
        self.__start_time = start_time
        self.__end_time = end_time

    def __str__(self) -> str:
        return f"PeriodCondition: {self.__day_of_week}, {self.__start_time}, {self.__end_time}"

    def is_satisfied_by(self, screening: "Screening") -> bool:
        return (
            self.__day_of_week == screening.get_when_screened().weekday()
            and self.__start_time <= screening.get_when_screened().time()
            and self.__end_time >= screening.get_when_screened().time()
        )
