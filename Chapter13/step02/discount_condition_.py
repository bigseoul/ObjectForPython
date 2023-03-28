from abc import *


class AbsDiscountCondition(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied_by(self, screening):
        pass
