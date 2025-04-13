from datetime import datetime, time, timedelta
from day_of_weeks_ import DAY_OF_WEEK
from money_ import Money
from call_ import Call
from phone_ import Phone
from basic_rate_policy_ import BasicRatePolicy
from fee_rule_ import FeeRule
from fee_per_duration_ import FeePerDuration
from time_of_day_fee_condition_ import TimeOfDayFeeCondition
from day_of_week_fee_condition_ import DayOfWeekFeeCondition
from duration_fee_condition_ import DurationFeeCondition

if __name__ == "__main__":

    #시간대별 정책

    call_1 = Call(datetime(2023, 1, 28, 8, 00, 00), datetime(2023, 1, 28, 10, 00, 00))
    call_2 = Call(datetime(2023, 1, 28, 12, 00, 00), datetime(2023, 1, 28, 14, 00, 00))

    tod_0_to_9 = TimeOfDayFeeCondition(time(00, 00, 00), time(8, 59, 59, 999999))
    fpd_0_to_9 = FeePerDuration(Money.wons(10), timedelta(seconds=10))
    fr_0_to_9 = FeeRule(tod_0_to_9, fpd_0_to_9)

    tod_9_to_24 = TimeOfDayFeeCondition(time(9, 00, 00), time(23, 59, 59, 999999))
    fpd_9_to_24 = FeePerDuration(Money.wons(20), timedelta(seconds=10))
    fr_9_to_24 = FeeRule(tod_9_to_24, fpd_9_to_24)

    bp_tod = BasicRatePolicy(fr_0_to_9, fr_9_to_24)
    phone_tod = Phone(bp_tod)
    phone_tod.call(call_1)
    print(phone_tod.calculate_fee().check_amount())
    

    """요일별 정책
    call_3 = Call(datetime(2023, 2, 10, 23, 00, 00), datetime(2023, 2, 11, 1, 00, 00))
    call_4 = Call(datetime(2023, 2, 10, 23, 00, 00), datetime(2023, 2, 11, 1, 00, 00))

    dow_sat_to_sun = DayOfWeekFeeCondition(
        DAY_OF_WEEK.get("Saturday"), DAY_OF_WEEK.get("Sunday")
    )
    fpd_sat_to_sun = FeePerDuration(Money.wons(10), timedelta(seconds=10))
    fr_sat_to_sun = FeeRule(dow_sat_to_sun, fpd_sat_to_sun)

    dow_mon_to_fri = DayOfWeekFeeCondition(
        DAY_OF_WEEK.get("Monday"),
        DAY_OF_WEEK.get("Tuesday"),
        DAY_OF_WEEK.get("Wednesday"),
        DAY_OF_WEEK.get("Thursday"),
        DAY_OF_WEEK.get("Friday"),
    )
    fpd_mon_to_fri = FeePerDuration(Money.wons(20), timedelta(seconds=10))
    fr_mon_to_fri = FeeRule(dow_mon_to_fri, fpd_mon_to_fri)

    bp_dow = BasicRatePolicy(fr_sat_to_sun, fr_mon_to_fri)
    phone_dow = Phone(bp_dow)
    phone_dow.call(call_3)
    print(phone_dow.calculate_fee().check_amount())
    """

    "구간별 정책"
    # call_5 = Call(datetime(2023, 2, 10, 22, 00, 00), datetime(2023, 2, 10, 23, 0, 0))
    # call_6 = Call(datetime(2023, 2, 10, 23, 00, 00), datetime(2023, 2, 11, 1, 00, 00))

    # df_0_to_59 = DurationFeeCondition(timedelta(seconds=0), timedelta(seconds=59))
    # df_60_to_119 = DurationFeeCondition(timedelta(seconds=60), timedelta(seconds=119))
    # df_120_to_max = DurationFeeCondition(timedelta(seconds=120), timedelta.max)

    # fpd_0_to_59 = FeePerDuration(Money.wons(50), timedelta(seconds=10))
    # fpd_60_to_119 = FeePerDuration(Money.wons(30), timedelta(seconds=10))
    # fpd_120_to_max = FeePerDuration(Money.wons(10), timedelta(seconds=10))

    # fr_0_to_59 = FeeRule(df_0_to_59, fpd_0_to_59)
    # fr_0_to_119 = FeeRule(df_60_to_119, fpd_60_to_119)
    # fr_120_to_max = FeeRule(df_120_to_max, fpd_120_to_max)

    # bp_df = BasicRatePolicy(fr_0_to_59, fr_0_to_119, fr_120_to_max)
    # phone_df = Phone(bp_df)
    # phone_df.call(call_5)

    # print(phone_df.calculate_fee().check_amount())
