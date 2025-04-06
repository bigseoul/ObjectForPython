from datetime import timedelta
from decimal import Decimal
from typing import List

from models import Call, Money, Phone

class BasicRatePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        return self._calculate_call_fee(phone.calls)
    
    def _calculate_call_fee(self, calls: List[Call]) -> Money:
        raise NotImplementedError

class RegularPolicy(BasicRatePolicy):
    def __init__(self, amount: Money, seconds: timedelta):
        self.amount = amount
        self.seconds = seconds
    
    def _calculate_call_fee(self, calls: List[Call]) -> Money:
        result = Money(Decimal('0'))
        for call in calls:
            duration = call.to_time - call.from_time
            unit = (duration.total_seconds() / self.seconds.total_seconds())
            result += self.amount * unit
        return result

class TaxablePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        fee = super().calculate_fee(phone)
        return fee + (fee * Decimal(str(self.tax_rate)))

class RateDiscountablePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        fee = super().calculate_fee(phone)
        return fee - self.discount_amount

class TaxableRegularPolicy(TaxablePolicy, RegularPolicy):
    def __init__(self, amount: Money, seconds: timedelta, tax_rate: float):
        super().__init__(amount, seconds)
        self.tax_rate = tax_rate

class RateDiscountableAndTaxableRegularPolicy(TaxablePolicy, RateDiscountablePolicy, RegularPolicy):
    def __init__(self, amount: Money, seconds: timedelta, discount_amount: Money, tax_rate: float):
        super().__init__(amount, seconds)
        self.discount_amount = discount_amount
        self.tax_rate = tax_rate 