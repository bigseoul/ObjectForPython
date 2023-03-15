from datetime import date, datetime

from discount_condition_type_ import DiscountConditionType
from multipledispatch import dispatch


class DiscountCondition:
    """
    2. step1에서 관리할 데이터를 결정해 놓음.
    """

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
    2. 위 데이터에 대해 수행할 수 있는 오퍼레이션이 무엇인가를 묻는 것. 
    기간 조건일 경우와 순번 조건을 경우를 구분할 is_discountable()이 필요함.
    
    파이썬은 overload가 없어서 아래의 라이브러리를 이용햇음.
    overloading libary
    https://www.geeksforgeeks.org/python-method-overloading/

    DiscountCondition의 isDiscountable(DayOfWeek, LocalTime)은 내부 인스턴스 변수의 타입을 인터페이스로 외부에 노출함
    이 메서드는 객체 내부에 DayOfWeek, LocalTime 정보가 인스턴스 변수로 포함돼 있음을 노출시킨다.
    setType 메서드는 없지만, getType 메서드를 통해 내부에 DiscountConditionType 인스턴스 변수가 있음을 노출한다.

    만약 DiscountCondition의 속성을 변경해야 한다면 어떻게 될까?
    아마 두 isDiscountable 메서드의 파라미터를 수정하고, 해당 메서드를 사용하는 모든 Client를 수정해야 할 것 이다.
    => 내부 구현의 변경이 외부로 퍼져나가는 파급효과(ripple effect)는 캡슐화 위반의 증거이다.
    
    """

    @dispatch(int, datetime)
    def is_discountable(self, day_of_week, time) -> bool:  # type: ignore
        if self.__dc_type != DiscountConditionType.PERIOD:
            raise ValueError("Wrong DC type for PERIOD")
        return (
            self.__day_of_week == day_of_week
            and self.__start_time <= time
            and self.__end_time >= time
        )

    @dispatch(int)
    def is_discountable(self, sequence) -> bool:  # type: ignore
        if self.__dc_type != DiscountConditionType.SEQUENCE:
            raise ValueError("Wrong DC type for SEQUENCE")
        return self.__sequence == sequence
