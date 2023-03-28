import logging
from day_of_weeks_ import DAY_OF_WEEK
from call_ import Call
from money_ import Money
from datetime import datetime, time, timedelta, date
from phone_ import Phone
from fixed_fee_policy_ import FixedFeePolicy
from nightly_discount_policy_ import NightlyDiscountPolicy
from taxable_policy_ import TaxablePolicy
from rate_discountable_policy_ import RateDiscountablePolicy
from date_time_interval_ import DateTimeInterval
from time_of_day_discount_policy_ import TimeOfDayDiscountPolicy
from day_of_week_discount_rule_ import DayOfWeekDiscountRule
from day_of_week_discount_policy_ import DayOfWeekDiscountPolicy
from duration_discount_rule_ import DurationDiscountRule

if __name__ == "__main__":

    # call_1 = Call(datetime(2023, 1, 23, 0, 0, 0), datetime(2023, 1, 23, 23, 59, 59))

    # phone = Phone(TaxablePolicy(0.01, RegularPolicy(Money.wons(10), time(0, 0, 10))))
    # phone.call(call)
    # print(phone.calculate_fee().check_amount())
    """생성자 생성 순서는 안에서부터"""
    # phone = Phone(
    #     RateDiscountablePolicy(
    #         Money.wons(1000),
    #         TaxablePolicy(0.01, FixedFeePolicy(Money.wons(1000), time(0, 0, 10))),
    #     )
    # )

    # phone.call(call)
    # print(phone.calculate_fee().check_amount())

    """
    시간대별 방식
    인덱스 0은 제대로 작동, 인덱스 1이 문제 ㅋ. 없는 걸 뺄라닊;; 
    """
    # call = Call(datetime(2023, 1, 10, 10, 00, 00), datetime(2023, 1, 12, 1, 0, 00))

    # starts = [time(00, 00, 00), time(18, 59, 59)]
    # ends = [time(19, 00, 00), time(23, 59, 59)]
    # durations = [timedelta(seconds=10), timedelta(seconds=10)]
    # amounts = [Money.wons(18), Money.wons(10)]

    # tdp = TimeOfDayDiscountPolicy(starts, ends, durations, amounts)

    # phone = Phone(tdp)
    # phone.call(call)
    # print(phone.calculate_fee().check_amount())

    """요일별 방식"""
    # call = Call(datetime(2023, 1, 28, 10, 00, 00), datetime(2023, 1, 29, 1, 0, 00))
    # dowd = DayOfWeekDiscountRule(
    #     [DAY_OF_WEEK.get("Saturday"), DAY_OF_WEEK.get("Sunday")],
    #     timedelta(seconds=10),
    #     Money.wons(10),
    # )
    # # print(dowd.calculate(call.get_interval()).check_amount())

    # dowdp = DayOfWeekDiscountPolicy([dowd])
    # phone = Phone(dowdp)
    # phone.call(call)
    # print(phone.calculate_fee().check_amount())

    """
    구간별 방식, from_time, to_time에 어떤 인자를 넣어야 할 지 모르겠음
    두번째 인자가 구간기준 시간인듯. 
    긁적;;
    """
    call = Call(datetime(2023, 1, 28, 10, 00, 00), datetime(2023, 1, 28, 10, 1, 00))

    ddr = DurationDiscountRule(
        Money.wons(10), time(0, 1), timedelta(seconds=70), timedelta(seconds=90)
    )

    print(ddr.calculate(call).check_amount())
