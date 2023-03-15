from decimal import Decimal

# Define a class called Money
class Money:
    # Constructor method that initializes the amount attribute with a Decimal value
    def __init__(self, amount: Decimal):
        self.amount = amount

    # String representation of the object
    def __str__(self):
        return f"요금: {self.amount}"

    # Class method that creates a Money object from a given integer amount in Korean won
    @classmethod
    def from_wons(cls, amount: int):
        return cls(Decimal(str(amount)))

    # Overloading the addition operator to add two Money objects
    def __add__(self, other: "Money"):
        return Money(self.amount + other.amount)

    # Overloading the subtraction operator to subtract two Money objects
    def __sub__(self, other: "Money"):
        return Money(self.amount - other.amount)

    # Overloading the multiplication operator to multiply a Money object by a percentage
    def __mul__(self, percent: float):
        return Money(self.amount * Decimal(str(percent)))

    # Overloading the less than operator to compare two Money objects
    def __lt__(self, other: "Money"):
        return self.amount < other.amount

    # Overloading the greater than or equal to operator to compare two Money objects
    def __ge__(self, other: "Money"):
        return self.amount >= other.amount
