from call_ import Call
from money_ import Money
from datetime import datetime, time
from phone_ import Phone
from regular_policy_ import RegularPolicy
from nightly_discount_policy_ import NightlyDiscountPolicy

if __name__ == "__main__":

    call = Call(datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 10, 31, 0))

    phone = Phone(RegularPolicy(Money.wons(10), time(0, 0, 10)))
    phone.call(call)
    print(phone.calculate_fee().check_amount())

    call2 = Call(datetime(2022, 12, 15, 22, 30, 0), datetime(2022, 12, 15, 22, 31, 0))

    phone2 = Phone(NightlyDiscountPolicy(Money.wons(5), Money.wons(10), time(0, 0, 10)))
    phone2.call(call2)
    print(phone2.calculate_fee().check_amount())
