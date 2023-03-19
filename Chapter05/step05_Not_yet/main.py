from datetime import datetime, time

from amount_discount_movie_ import AmountDiscountMovie
from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from money_ import Money
from none_discount_movie_ import NoneDiscountMovie
from percent_discount_movie_ import PercentDiscountMovie
from period_condition_ import PeriodCondition
from screening_ import Screening
from sequence_condition_ import SquenceCondition

if __name__ == "__main__":

    """순번 조건, 1회차 대상"""
    sq_condition1 = SquenceCondition(1)

    """기간 조건, 금요일, 8월 17시~21시까지, 0은 nothing"""
    period_condition1 = PeriodCondition(
        DAY_OF_WEEKS.get("Monday"), time(9, 00), time(19, 00)
    )

    the_batman = AmountDiscountMovie(
        "the batman",
        time(1, 53),
        Money.from_wons(18000),
        Money.from_wons(10000),
        sq_condition1,
        period_condition1,
    )
    screening = Screening(the_batman, 1, datetime(2022, 11, 14, 18, 30, 0))

    the_batman2 = PercentDiscountMovie(
        "the batman",
        time(1, 53),
        Money.from_wons(18000),
        0.1,
        sq_condition1,
        period_condition1,
    )
    screening2 = Screening(the_batman2, 1, datetime(2022, 11, 14, 18, 30, 0))

    the_batman3 = NoneDiscountMovie(
        "the batman",
        time(1, 53),
        Money.from_wons(18000),
        sq_condition1,
        period_condition1,
    )
    screening3 = Screening(the_batman3, 1, datetime(2022, 11, 14, 18, 30, 0))

    reservation = screening.reserve(Customer("steve", 101), 2)
    reservation2 = screening2.reserve(Customer("dave", 102), 1)
    reservation3 = screening3.reserve(Customer("miz", 103), 2)

    print(reservation3)
