from decimal import Decimal
from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from money_ import Money


class Money:

    # ZERO = Money.from_wons(0)

    def __init__(self, amount: Decimal) -> None:
        self.__amount = amount

    def __str__(self) -> str:
        return f"요금: {self.__amount}"

    @classmethod
    def from_wons(cls, amount: int) -> "Money":
        return cls(Decimal(str(amount)))

    def plus(self, amount: "Money") -> "Money":
        return Money(self.__amount + amount.__amount)

    def minus(self, amount: "Money") -> "Money":
        return Money(self.__amount - amount.__amount)

    def times(self, percent: float) -> "Money":
        return Money(self.__amount * Decimal(str(percent)))

    def is_less_than(self, other: "Money") -> bool:
        return self.__amount < other.__amount

    def is_greater_than_or_equal(self, other: "Money") -> bool:
        return self.__amount >= other.__amount
