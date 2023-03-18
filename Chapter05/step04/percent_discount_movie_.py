from typing import TYPE_CHECKING
from movie_ import AbsMovie
from money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    
class PercentDiscountMovie(AbsMovie):
    
    def __init__(self, title, running_time, fee: "Money", percent, *discount_conditions: "AbsDiscountCondition") -> None:
        super().__init__(title, running_time, fee, *discount_conditions)
        self.__percent = percent
        
    def _calculate_discount_amount(self):
        temp = self._getFee().times(self.__percent)
        return temp