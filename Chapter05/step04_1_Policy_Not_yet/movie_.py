"""
1. 영화 비용을 계산할 책임이 있음.
2. 영화 정보, 가격, 할인 정책, 할인 비용 정도 가지고 있음.
"""
import logging
logging.basicConfig(level=logging.INFO)

from abc import *
from money_ import Money
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening
    from discount_condition_ import AbsDiscountCondition
    from period_condition_ import PeriodCondition
    from sequence_condition_ import SquenceCondition


    """ 
    self.__period_conditions = period_conditions
    self.__squence_conditions = squence_conditions
    //메인에서 리스트로 던져서 보내야 하나?
    // [sq1, sq2] 이렇게 묶어서 보낸다. list(sq1, sq2) 아님
    """

class AbsMovie(metaclass=ABCMeta):
    def __init__(
        self,
        title,
        running_time,
        fee: "Money",
        *discount_conditions: "AbsDiscountCondition",
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__running_time = running_time 
        self.__discount_conditions = list(discount_conditions)

    def calculate_movie_fee(self, screening) -> Money:
        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        # 4-1
        if self.__is_discountable(screening) == True:
            return self.__fee.minus(
                self._calculate_discount_amount()
            )  # Money타입으로 리턴할 거임.

    """step03 """
    def __is_discountable(self, screening: "Screening") -> bool :
        result = False
        for condition in self.__discount_conditions:
            temp_condition: "AbsDiscountCondition" = condition
            if temp_condition.is_satisfied_by(screening) == True:
                result = True
        return result

    """분기문, 수정에 취약, 폴리모피즘-프로텍티드 베리에이션 적용"""
    @abstractmethod
    def _calculate_discount_amount(self):
        pass
    
    def _getFee(self) -> "Money":
        return self.__fee