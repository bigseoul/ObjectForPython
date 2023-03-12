from decimal import Decimal
from typing import TYPE_CHECKING


from decimal import Decimal

# Define a class named Money
class Money:
    # Constructor method to initialize the class with an amount of type Decimal
    def __init__(self, amount: Decimal) -> None:
        self.__amount = amount

    # Method to return a string representation of the amount
    def __str__(self) -> str:
        return f"요금: {self.__amount}"

    # Class method to create a new instance of Money from an amount in Korean won
    @classmethod
    def from_wons(cls, amount: int) -> "Money":
        return cls(Decimal(str(amount)))

    # Method to add two Money objects and return a new Money object with the sum
    def plus(self, amount: "Money") -> "Money":
        return Money(self.__amount + amount.__amount)

    # Method to subtract one Money object from another and return a new Money object with the difference
    def minus(self, amount: "Money") -> "Money":
        return Money(self.__amount - amount.__amount)

    # Method to multiply a Money object by a percentage and return a new Money object with the result
    def times(self, percent: float) -> "Money":
        return Money(self.__amount * Decimal(str(percent)))

    # Method to check if the amount of one Money object is less than the amount of another Money object
    def is_less_than(self, other: "Money") -> bool:
        return self.__amount < other.__amount

    # Method to check if the amount of one Money object is greater than or equal to the amount of another Money object
    def is_greater_than_or_equal(self, other: "Money") -> bool:
        return self.__amount >= other.__amount
