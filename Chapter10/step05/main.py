from datetime import datetime, time

from call_ import Call
from money_ import Money
from nightly_discount_phone_ import NightlyDiscountPhone
from phone_ import Phone

if __name__ == "__main__":
    call_1 = Call(
        datetime(2022, 12, 15, 21, 59, 20), datetime(2022, 12, 15, 22, 00, 00)
    )

    call_2 = Call(datetime(2022, 12, 15, 22, 1, 00), datetime(2022, 12, 15, 22, 1, 50))
    phone_night = NightlyDiscountPhone(Money(2), Money(5), time(0, 0, 10), 0.1)
    phone_night.call(call_1)
    phone_night.call(call_2)

    print(phone_night.calculate_fee().check_amount())
