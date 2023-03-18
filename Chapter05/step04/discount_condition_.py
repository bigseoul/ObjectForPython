from abc import *
from discount_condition_type_ import DiscountConditionType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening

"""
1. 조건을 확인한다.
2. 할인정책 종류 정보, 정책별()
"""


class AbsDiscountCondition(metaclass=ABCMeta):
    
    @abstractmethod
    def is_satisfied_by(self, screening: "Screening"):
        pass