from call_ import Call
from money_ import Money
from datetime import datetime, time
from phone_ import Phone
from regular_policy_ import RegularPolicy
from nightly_discount_policy_ import NightlyDiscountPolicy
from taxable_policy_ import TaxablePolicy
from rate_discountable_policy_ import RateDiscountablePolicy

if __name__ == "__main__":

    call = Call(datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 11, 30, 0))

    # regular_policy = RegularPolicy(Money.wons(10), time(0, 0, 10))  # 10초당 10원
    # phone = Phone(regular_policy)  # Phone에 RegularPolicy 주입
    # phone = Phone(TaxablePolicy(0.01, RegularPolicy(Money.wons(10), time(0, 0, 10))))
    # phone.call(call)
    # print(phone.calculate_fee().check_amount())
    """생성자 생성 순서는 안에서부터 """
    # phone = Phone(
    #     RateDiscountablePolicy(
    #         Money.wons(1000),
    #         TaxablePolicy(0.01, RegularPolicy(Money.wons(1000), time(0, 0, 10))),
    #     )
    # )

    #일반 요금제
    regular_policy = RegularPolicy(Money.wons(10), time(second=5))

    # 할인 정책 20% 적용RateDiscountablePolicy
    rate_discount_policy = (0.2, regular_policy)

    #세금 정책 10% 적용
    tax_policy = TaxablePolicy(0.1, rate_discount_policy)
    #전화기에 최종 정책 설정
    
    phone = Phone(tax_policy)

    #전화 걸기
    phone.call(call)
    print(phone.calculate_fee().check_amount())
