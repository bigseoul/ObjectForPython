from abc import ABCMeta, abstractmethod


class AbsDiscountCondition(metaclass=ABCMeta):
    """파이썬은 인터페이스가 없으므로 추상클래스로 구현"""

    @abstractmethod
    def is_satisfied_by(self, screening):
        pass
