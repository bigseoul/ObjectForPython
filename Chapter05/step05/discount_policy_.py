from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from discount_condition_ import AbsDiscountCondition
from money_ import Money

if TYPE_CHECKING:
    from discount_condition_ import AbsDiscountCondition
    from screening_ import Screening


class DiscountPolicy(metaclass=ABCMeta):
    def __init__(self, *args: AbsDiscountCondition) -> None:
        self._discount_condtions = list(args)  # __을 쓰면, 자식 객체에서 호출 못함.

    def __str__(self) -> str:
        return f"할인정책/조건:{self} / {self._discount_condtions}"

    def calculate_discount_amount(self, screening: "Screening") -> Money:
        """
        1. condition 리스트 정보와 상영영화 정보를 확인.
        2. conditon이 SquenceCondition일 경우...알아서 찾아 들어감. 레이지 바이딩
        3. is_satisfied_by() 인자에 screening넘김. (상영정보가 있음.)
        """
        for conditon in self._discount_condtions:
            if conditon.is_satisfied_by(screening):
                return self._get_discount_amount(screening)

        return Money.from_wons(0)

    @abstractmethod
    def _get_discount_amount(self, screening) -> Money:
        """screening은 PercentDiscountPolicy때문. 여기서 영화요금에 비율로 나눠야 함."""
        pass
