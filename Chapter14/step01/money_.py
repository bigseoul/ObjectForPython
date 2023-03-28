import math
from decimal import Decimal
from pickle import NONE
from typing import TYPE_CHECKING

# from money_ import Money

# if TYPE_CHECKING:
#     from step01.money_ import Money

class Money:
  
    @staticmethod
    def wons(amount: int) -> "Money":
        return Money(Decimal(str(amount)))

    def __init__(self, amount: Decimal) -> None:
        self.__amount = amount

    def plus(self, amount: "Money"):
        return Money(self.__amount + amount.__amount)

    def minus(self, amount: "Money"):
        return Money(self.__amount - amount.__amount)

    def times(self, percent: float):
        return Money(self.__amount * Decimal(str(percent)))

    def is_less_than(self, other: "Money"):
        return self.__amount < other.__amount

    def is_greater_than_or_equal(self, other: "Money"):
        return self.__amount >= other.__amount

    def check_amount(self):
        return self.__amount
