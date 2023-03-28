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
    # phone = Phone(TaxablePolicy(0.01, RegularPolicy(Money.wons(10), time(0, 0, 10))))
    # phone.call(call)
    # print(phone.calculate_fee().check_amount())
    """생성자 생성 순서는 안에서부터 """
    phone = Phone(
        RateDiscountablePolicy(
            Money.wons(1000),
            TaxablePolicy(0.01, RegularPolicy(Money.wons(1000), time(0, 0, 10))),
        )
    )

    phone.call(call)
    print(phone.calculate_fee().check_amount())
