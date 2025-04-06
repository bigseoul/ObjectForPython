from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List

@dataclass
class Call:
    from_time: datetime
    to_time: datetime

@dataclass
class Money:
    amount: Decimal
    
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return Money(self.amount + other)
    
    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        return Money(self.amount - other)
    
    def __mul__(self, other):
        return Money(self.amount * Decimal(str(other)))

@dataclass
class Phone:
    calls: List[Call] 