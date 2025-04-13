from datetime import datetime, timedelta
from decimal import Decimal
from typing import List

from models import Call, Money, Phone

class BasicRatePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        print("\n1. BasicRatePolicy.calculate_fee 시작")
        result = self._calculate_call_fee(phone.calls)
        print("6. BasicRatePolicy.calculate_fee 종료, 반환값:", result.amount)
        return result
     
    def _calculate_call_fee(self, calls: List[Call]) -> Money:
        print("2. BasicRatePolicy._calculate_call_fee 호출")
        print("3. 기본 요금 계산 중...")
        result = Money(Decimal('100'))  # 테스트를 위한 고정값
        print("4. 기본 요금 계산 완료:", result.amount)
        print("5. BasicRatePolicy._calculate_call_fee 종료")
        return result

class RegularPolicy(BasicRatePolicy):
    def __init__(self, amount: Money, seconds: timedelta):
        self.amount = amount
        self.seconds = seconds
    
    def calculate_fee(self, phone: Phone) -> Money:
        print("\n7. RegularPolicy.calculate_fee 시작")
        result = super().calculate_fee(phone)
        print("8. RegularPolicy.calculate_fee 종료, 반환값:", result.amount)
        return result

class TaxablePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        print("\n9. TaxablePolicy.calculate_fee 시작")
        fee = super().calculate_fee(phone)
        print("10. 세금 계산 중...")
        result = fee + (fee * Decimal(str(self.tax_rate)))
        print("11. TaxablePolicy.calculate_fee 종료, 반환값:", result.amount)
        return result

class RateDiscountablePolicy:
    def calculate_fee(self, phone: Phone) -> Money:
        print("\n12. RateDiscountablePolicy.calculate_fee 시작")
        fee = super().calculate_fee(phone)
        print("13. 할인 계산 중...")
        result = fee - self.discount_amount
        print("14. RateDiscountablePolicy.calculate_fee 종료, 반환값:", result.amount)
        return result

class RateDiscountableAndTaxableRegularPolicy(TaxablePolicy, RateDiscountablePolicy, RegularPolicy):
    def __init__(self, amount: Money, seconds: timedelta, discount_amount: Money, tax_rate: float):
        super().__init__(amount, seconds)
        self.discount_amount = discount_amount
        self.tax_rate = tax_rate

if __name__ == "__main__":
    # MRO 출력
    print("Method Resolution Order (MRO):")
    for i, cls in enumerate(RateDiscountableAndTaxableRegularPolicy.__mro__):
        print(f"{i+1}. {cls.__name__}")
    
    # 테스트용 통화 기록 생성
    calls = [
        Call(
            from_time=datetime(2024, 1, 1, 10, 0),
            to_time=datetime(2024, 1, 1, 10, 1)
        )
    ]
    phone = Phone(calls=calls)
    
    # 정책 객체 생성 및 요금 계산
    print("\n=== 요금 계산 시작 ===")
    policy = RateDiscountableAndTaxableRegularPolicy(
        amount=Money(Decimal('10')),
        seconds=timedelta(minutes=1),
        discount_amount=Money(Decimal('5')),
        tax_rate=0.1
    )
    
    result = policy.calculate_fee(phone)
    print("\n=== 최종 요금 ===")
    print(f"Final result: {result.amount}") 