from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    from period_condition_ import PeriodCondition
    from screening_ import Screening
    from sequence_condition_ import SquenceCondition


class AbsMovie(ABC):
    def __init__(
        self,
        title,
        running_time,
        fee: Money,
        *discount_conditions: "AbsDiscountCondition",
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__running_time = running_time
        self.__discount_conditions = list(discount_conditions)

    def calculate_movie_fee(self, screening) -> Money:
        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        # 4-1
        if self.__is_discountable(screening):
            return self.__fee - self._calculate_discount_amount()  # Money타입으로 리턴할 거임.
        else:
            return self.__fee

    """step03 """

    def __is_discountable(self, screening: "Screening") -> bool:
        return any(
            condition.is_satisfied_by(screening)
            for condition in self.__discount_conditions
        )

    """
    분기문, 수정에 취약, 폴리모피즘-프로텍티드 베리에이션 적용
    객체 변수가 상위 클래스인 AbsDiscountCondition를 가리키고 있지만, 
    메서드 호출할 때는 같은 이름을 가진 자식을 호출함. //맴버 필드는 현재 참조점의 것.
    """

    @abstractmethod
    def _calculate_discount_amount(self) -> Money:
        pass

    def _getFee(self) -> "Money":
        return self.__fee
