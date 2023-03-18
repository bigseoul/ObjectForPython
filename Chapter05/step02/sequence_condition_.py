from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening

class SquenceCondition:
    
    def __init__(self, sequence) -> None:
        self.__sequence = sequence
        
    def is_satisfied_by(self, screening: "Screening") -> bool:
        return self.__sequence == screening.get_sequence()
