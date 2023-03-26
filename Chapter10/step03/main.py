from datetime import datetime, time
from call_ import Call
from money_ import Money
from phone_ import Phone

if __name__ == "__main__":

    call_regular = Call(
        datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 10, 31, 0)
    )

    phone_regular = Phone.from_phone_for_regular(Money.wons(5), time(0, 0, 10))
    phone_regular.call(call_regular)
    print("regular: ", phone_regular.calculate_fee().check_amount())

    call_night = Call(
        datetime(2022, 12, 15, 22, 30, 0), datetime(2022, 12, 15, 22, 31, 0)
    )

    phone_nightly = Phone.from_phone_for_nightly(
        Money.wons(2), Money.wons(5), time(0, 0, 10)
    )
    phone_nightly.call(call_night)
    print("nightly: ", phone_nightly.calculate_fee().check_amount())
