from time import time
from constant_ import DAY_OF_WEEK
from datetime import date, time, datetime

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discount_condition_type_ import DiscountConditionType


class DiscountCondition:
    def __init__(self) -> None:
        self.__type = None
        self.__sequence = None
        self.__day_of_week = None
        self.__start_time = None
        self.__end_time = None

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):
        self.__sequence = sequence

    @property
    def day_of_week(self):
        return self.__day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        self.__day_of_week = day_of_week

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def end_time(self) -> datetime:
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        self.__end_time = end_time
