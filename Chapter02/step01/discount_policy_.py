from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    from screening_ import Screening


class AbsDiscountPolicy(metaclass=ABCMeta):
    """
    부모 추상 클래스에 중복코드를 두고 자식 구체 클래스가 이를 상속 받도록 함.
    이처럼 부모 클래스에 기본적인 알고리즘의 흐름을 구현하고
    중간에 필요한 처리를 자식 클래스에게 위임하는 디자인 패턴을 TEMPLATE METHOD 패턴이라고 부른다.

    아는 것: 할인 조건들
    하는 것: (할인정책 구현 객체의 )정책을 바탕으로 할인 조건에 부합하는지 확인 한 뒤, 할인 함.
    """

    def __init__(self, *args: "AbsDiscountCondition") -> None:
        """
        discountPolicy는 discountCondition 인자 여러 개를 가질 수 있다.
        """
        self.__conditions = list(args)

    def __str__(self) -> str:
        return f"할인정책/조건:{self}, {self.__conditions}"

    def calculate_discount_amount(self, screening: "Screening") -> "Money":
        """
        NoneDisdountPolicy의 _get_discount_amount는 호출될 일 없음.
        왜냐하면, calculate_discount_amount 메서드 내에서 condotions가 없으면,
        _get_discount_amount를 호출하지 않음.

        step02에 변경사항 있음.
        """

        for condition in self.__conditions:
            if condition.is_satisfied_by(screening):
                return self._get_discount_amount(screening)

        return Money.from_wons(0)  # 할인 정책이 없는 경우를 예외 케이스로 취급하기에 지금까지 일관성 있던 협력 방식이 무너짐.

    @abstractmethod
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        pass
