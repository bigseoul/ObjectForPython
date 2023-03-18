from datetime import time
from typing import TYPE_CHECKING, Optional

from discount_condition_type_ import DiscountConditionType

if TYPE_CHECKING:
    from screening_ import Screening


class DiscountCondition:
    """
    1. 조건을 확인한다.
    2. 할인정책 종류 정보, 정책별()"""

    def __init__(
        self,
        condition_type: DiscountConditionType,
        sequence: int = 0,
        day_of_week: Optional[int] = 0,
        start_time: Optional[time] = None,
        end_time: Optional[time] = None,
    ) -> None:
        self.__type = condition_type
        self.__sequence = sequence
        self.__day_of_week = day_of_week
        self.__start_time = start_time
        self.__end_time = end_time

    def is_satisfied_by(self, screening) -> bool:
        if self.__type == DiscountConditionType.PERIOD_DISCOUNT:
            return self.__is_satisfied_by_period(screening)
        return self.__is_satisfied_by_sequence(screening)

    def __is_satisfied_by_period(self, screening: "Screening") -> bool:
        if self.__start_time is None or self.__end_time is None:
            return False

        return (
            self.__day_of_week == screening.get_when_screened().weekday()
            and self.__start_time <= screening.get_when_screened().time()
            and self.__end_time >= screening.get_when_screened().time()
        )

    def __is_satisfied_by_sequence(self, screeing: "Screening") -> bool:
        return self.__sequence == screeing.get_sequence()
