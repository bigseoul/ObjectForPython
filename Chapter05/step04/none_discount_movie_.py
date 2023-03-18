from typing import TYPE_CHECKING
from movie_ import AbsMovie
from money_ import Money
from money_zero import MoneyZero

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition

class NoneDiscountMovie(AbsMovie):
    
    def __init__(self, title, running_time, fee: "Money", *discount_conditions: "AbsDiscountCondition") -> None:
        super().__init__(title, running_time, fee, *discount_conditions)
        
    def _calculate_discount_amount(self):
        return MoneyZero.ZERO