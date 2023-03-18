from typing import TYPE_CHECKING

from movie_ import AbsMovie
from money_ import Money
if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition

class AmountDiscountMovie(AbsMovie):
    
    """discount_amount는 이 클래스의 인스턴스 변수"""
    def __init__(self, title, running_time, fee: "Money", discount_amount, *discount_conditions: "AbsDiscountCondition") -> None:
        super().__init__(title, running_time, fee, *discount_conditions)
        self.__discount_amount = discount_amount
        
    def _calculate_discount_amount(self) -> "Money":
        return self.__discount_amount