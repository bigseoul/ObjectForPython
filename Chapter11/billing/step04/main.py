from call_ import Call
from datetime import datetime, time
from regular_phone_ import RegularPhone
from nightly_discount_phone_ import NightlyDiscountPhone
from taxable_regular_phone_ import TaxableRegularPhone
from money_ import Money

if __name__ == "__main__":

    call = Call(datetime(2022, 12, 15, 10, 30, 0), datetime(2022, 12, 15, 10, 31, 0))

    phone = TaxableRegularPhone(Money.wons(5), time(0, 0, 10), 0.1)
    phone.call(call)
    print(phone.calculate_fee().check_amount())
    print(phone.after_calculated(phone.calculate_fee()).check_amount())
