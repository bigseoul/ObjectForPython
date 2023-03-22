from abc import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening


class AbsDiscountCondition(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied_by(self, screening: "Screening"):
        pass
