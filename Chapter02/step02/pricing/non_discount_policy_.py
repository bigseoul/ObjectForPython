import logging

from typing import TYPE_CHECKING
from discount_policy_ import AbsDiscountPolicy
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening


class NonDiscountPolicy(AbsDiscountPolicy):

    """Movie, calculate_discount_amount에서 return Money.wons(0) 가 처리해줌.
    패스해도 상관없음. 쓰질 않으니... 근데 왜 접근조차 안한는 거지?
    왜냐하면, 컨디션 있을 때만 접근하도록 해놨으니까..
    결국, movie객체에서 Money.wons(0)해도 상관없는 코드가 됨.

    movie객체에 컨디션 안들어가는 조건으로
    return self.get_discount_amount(screening) 해줌.
    """

    def get_discount_amount(self, screening: "Screening"):
        logging.warning("reservation 시작하자 마나 워닝이 뜨네??")
        return Money.wons(0)
