from msilib import sequence
from typing_extensions import Self
from constant_ import DAY_OF_WEEK
from datetime import date, time, datetime

from typing import TYPE_CHECKING
from multipledispatch import dispatch


if TYPE_CHECKING:
    from discount_condition_type_ import DiscountConditionType


class DiscountCondition:
    def __init__(
        self,
        dc_type: "DiscountConditionType",
        sequence=None,
        day_of_week=None,
        start_time=None,
        end_time=None,
    ) -> None:
        self.__dc_type = dc_type
        self.__sequence = sequence
        self.__day_of_week = day_of_week
        self.__start_time = start_time
        self.__end_time = end_time

    @classmethod
    def from_DC_for_sequence(cls, cls_sequence):
        return cls(dc_type=DiscountConditionType.SEQUENCE, sequence=cls_sequence)

    @classmethod
    def from_DC_for_peried(cls, cls_day_of_week, cls_start_time, cls_end_time):
        return cls(
            dc_type=DiscountConditionType.PERIOD,
            day_of_week=cls_day_of_week,
            start_time=cls_start_time,
            end_time=cls_end_time,
        )

    def get_type(self):
        return self.__dc_type

    """
    overloading lib
    https://www.geeksforgeeks.org/python-method-overloading/
    """

    @dispatch(int)
    def is_discountable(self, sequence) -> bool:
        if self.__dc_type != DiscountConditionType.SEQUENCE:
            raise ValueError("Wrong DC type for SEQUENCE")
        return self.__sequence == sequence

    # int <- DAY_OF_WEEK.get()
    @dispatch(int, datetime)
    def is_discountable(self, day_of_week, time) -> bool:
        if self.__dc_type != DiscountConditionType.PERIOD:
            raise ValueError("Wrong DC type for PERIOD")
        return (
            self.__day_of_week == day_of_week
            and self.__start_time <= time
            and self.__end_time >= time
        )
