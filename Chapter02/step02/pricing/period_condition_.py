from datetime import date, datetime, time
from typing import TYPE_CHECKING

from constant_ import DAY_OF_WEEKS
from discount_condition_ import AbsDiscountCondition

if TYPE_CHECKING:
    from screening_ import Screening


class PeriodCondition(AbsDiscountCondition):
    """
    아는 것: 조건에 쓸 요일, 시작 시간, 종료 시간
    하는 것: 상영조건이 할인조건에 맞는 지 확인해 bool로 리턴

    """

    def __init__(self, day_of_week, start_time: time, end_time: time) -> None:
        self.__day_of_week = day_of_week
        self.__start_time = start_time
        self.__end_time = end_time

    def __str__(self) -> str:
        return f"조건요일: {self.__day_of_week}\n시작시간: {self.__start_time}\n종료시간: {self.__end_time}"

    # override
    def is_satisfied_by(self, screening: "Screening"):
        """상영 요일이 dayOfWeek와 같고, 상영시간이 startTime과 endTime 사이에 있으면 True"""
        return (
            self.__day_of_week == screening.get_start_time().weekday()
            and self.__start_time <= screening.get_start_time().time()
            and self.__end_time >= screening.get_start_time().time()
        )
