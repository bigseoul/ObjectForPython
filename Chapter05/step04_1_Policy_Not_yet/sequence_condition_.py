from typing import TYPE_CHECKING
from discount_condition_ import AbsDiscountCondition


if TYPE_CHECKING:
    from screening_ import Screening

class SquenceCondition(AbsDiscountCondition):
    
    def __init__(self, sequence) -> None:
        self.__sequence = sequence
        
    def is_satisfied_by(self, screening: "Screening") -> bool:
        return self.__sequence == screening.get_sequence()
