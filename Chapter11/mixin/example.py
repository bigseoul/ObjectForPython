from datetime import datetime, timedelta
from decimal import Decimal

from models import Call, Money, Phone
from policies import RegularPolicy, TaxableRegularPolicy, RateDiscountableAndTaxableRegularPolicy

def main():
    # Create a phone with some calls
    calls = [
        Call(
            from_time=datetime(2024, 1, 1, 10, 0),
            to_time=datetime(2024, 1, 1, 10, 1)
        )
    ]
    phone = Phone(calls=calls)
    
    # Regular policy
    # regular_policy = RegularPolicy(
    #     amount=Money(Decimal('10')),
    #     seconds=timedelta(minutes=1)
    # )
    # print(f"Regular fee: {regular_policy.calculate_fee(phone).amount}")
    
    # Taxable regular policy
    # taxable_policy = TaxableRegularPolicy(
    #     amount=Money(Decimal('10')),
    #     seconds=timedelta(minutes=1),
    #     tax_rate=0.1
    # )
    # print(f"Taxable fee: {taxable_policy.calculate_fee(phone).amount}")
    
    #Rate discountable and taxable policy
    discountable_and_taxable_policy = RateDiscountableAndTaxableRegularPolicy(
        amount=Money(Decimal('10')),
        seconds=timedelta(minutes=1),
        discount_amount=Money(Decimal('5')),
        tax_rate=0.1
    )
    print(f"Discounted and taxable fee: {discountable_and_taxable_policy.calculate_fee(phone).amount}")
    print(RateDiscountableAndTaxableRegularPolicy.__mro__)

if __name__ == "__main__":
    main() 