from datetime import date, time, datetime
from typing import TYPE_CHECKING

from discount_policy_ import AbsDiscountPolicy
from discount_condition_ import AbsDiscountCondition
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening


class BrokenDiscountPolicy(AbsDiscountPolicy):
    def __init__(self, *args: AbsDiscountCondition) -> None:
        super().__init__(*args)

    # override
    def calculate_discount_amount(self, screening: "Screening"):
        self._check_precondition(screening)
        self.__check_stronger_precondition(screening)

        amount = screening.get_movie_fee()
        self._check_postcondition(amount)
        self.__check_stronger_postcondition(amount)
        return amount

    def __check_stronger_precondition(self, screening: "Screening"):
        movie_end_time = screening.get_end_time().time()

        assert movie_end_time <= time(23, 59), "영업시간 종료"

        # open_time = time(6, 00)
        # closed_time = time(23, 59)
        # assert movie_end_time <= closed_time and movie_end_time >= open_time, "영업시간 종료"

    def __check_stronger_postcondition(self, amount: Money):
        assert amount.is_greater_than_or_equal(Money.wons(1000))

    def __check_weaker_postcondition(self, amount: Money):
        assert amount != None

    # override
    def get_discount_amount(self, screening: "Screening") -> Money:
        return Money.wons(0)
