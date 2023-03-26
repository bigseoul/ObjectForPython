from call_ import Call
from datetime import datetime, time
from money_ import Money
from phone_ import Phone
from nightly_discount_phone_ import NightlyDiscountPhone

if __name__ == "__main__":

    # call_1 = Call(
    #     datetime(2022, 12, 15, 21, 59, 20), datetime(2022, 12, 15, 22, 00, 00)
    # )

    # call_2 = Call(datetime(2022, 12, 15, 22, 1, 00), datetime(2022, 12, 15, 22, 1, 50))
    # phone_night = NightlyDiscountPhone(Money(2), Money(5), time(0, 0, 10))
    # phone_night.call(call_1)
    # phone_night.call(call_2)

    # print(phone_night.calculate_fee().check_amount())
    call_normal = Call(
        datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 10, 31, 0)
    )

    phone_normal = Phone(Money.wons(5), time(0, 0, 10))
    phone_normal.call(call_normal)
    print(phone_normal.get_calls())
    print(phone_normal.calculate_fee().check_amount())

    call_night = Call(
        datetime(2022, 12, 15, 22, 30, 0), datetime(2022, 12, 15, 22, 31, 0)
    )
    phone_night = NightlyDiscountPhone(Money.wons(2), Money.wons(5), time(0, 0, 10))
    phone_night.call(call_night)
    print(phone_night.calculate_fee().check_amount())
