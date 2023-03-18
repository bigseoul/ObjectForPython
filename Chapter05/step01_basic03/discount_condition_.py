import logging
from datetime import time
from typing import TYPE_CHECKING, Optional

from discount_condition_type_ import DiscountConditionType

if TYPE_CHECKING:
    from screening_ import Screening


class DiscountCondition:

    """
    1. 조건을 확인한다.
    2. 할인정책 종류 정보, 정책별()
    """

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

    def __str__(self) -> str:
        return (
            f"DiscountCondition("
            f"type={self.__type}, "
            f"sequence={self.__sequence}, "
            f"day_of_week={self.__day_of_week}, "
            f"start_time={self.__start_time}, "
            f"end_time={self.__end_time})"
        )

    def is_satisfied_by(self, screening) -> bool:
        """
        문제점) => STEP02
        지금의 DiscountCondition은 서로 다른 3가지 이유로 변경될수가 있다.
        => SRP(단일 책임 원칙) 위배

        새로운 할인 조건을 추가할 경우
        => isSatisfiedBy 안에 if ~ else 구문을 수정해야함.

        순번 조건을 판단하는 로직 변경
        => isSatisfiedBySequence 메서드 내부 구현을 수정해야 한다.

        기간 조건을 판단하는 로직이 변경되는 경우
        => isStatisfiedByPeriod 메서드의 내부 구현을 수정해야 한다.

        DiscountCondition은 하나 이상의 변경 이유를 가지기 때문에 응집도가 낮다.
        => 변경의 이유에 따라 클래스를 분리해야 한다.


        1) 인스턴스 변수 초기화 시점 살피기

        코드를 통해 변경의 이유를 파악할 수 있는 첫번째 방법은 인스턴스 변수가 초기화되는 시점 을 살펴보는것 이다.

        응집도가 높은 클래스는 인스턴스를 생성할떄 모든 속성을 함께 초기화한다.

        반면 응집도가 낮은 클래스는 일부만 초기화 하고, 나머지는 초기화 하지 않은 상태로 둔다.

        따라서 함께 초기화 되는 속성을 기준으로 코드를 분리해야 한다.


        2) 메서드가 인스턴스 변수를 사용하는 방식

        모든 메서드가 객체의 모든 속성을 사용한다면 클래스의 응집도는 높다고 볼 수 있다.

        반면 메서드들이 사용하는 속성에 따라 그룹이 나뉜다면 클래스의 응집도는 낮다고 볼 수 있다.

        예를 들어 isSatisfiedBySequence 메서드는 sequence 는 사용하지만 dayOfWeek, startTime, endTime은 사용하지 않는다.

        반대로 isStatisfiedByPeriod 메서드는 dayOfWeek, startTime, endTime은 사용하지만 sequence는 사용하지 않는다.

        """

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
