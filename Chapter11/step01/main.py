from call_ import Call
from datetime import datetime, time
from regular_phone_ import RegularPhone
from nightly_discount_phone_ import NightlyDiscountPhone
from money_ import Money

if __name__ == "__main__":

    call_normal = Call(
        datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 10, 31, 0)
    )

    phone_normal = RegularPhone(Money.wons(5), time(0, 0, 10))
    phone_normal.call(call_normal)
    print(phone_normal.calculate_fee().check_amount())

    call_night = Call(
        datetime(2022, 12, 15, 22, 30, 0), datetime(2022, 12, 15, 22, 31, 0)
    )
    phone_night = NightlyDiscountPhone(Money.wons(2), Money.wons(5), time(0, 0, 10))
    phone_night.call(call_night)
    print(phone_night.calculate_fee().check_amount())
