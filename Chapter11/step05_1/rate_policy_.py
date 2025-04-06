from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from money_ import Money
from call_ import Call

if TYPE_CHECKING:
    from phone_ import Phone

"""
폰에서 요금 계산 방법을 분리
RatePolicy는 Phone을 인자로 받아 계산한 요금을 반환한다.

최상위 추상클래스, 베이직과 에디셔널 추상이 상속받음
calculate_fee 메서드는 베이직과 에니셔널의 공통요소
"""


class RatePolicy(metaclass=ABCMeta):
    @abstractmethod
    def calculate_fee(self, phone: "Phone") -> Money:
        ...
