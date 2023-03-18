import logging

logging.basicConfig(level=logging.INFO)

from datetime import datetime, time

from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from money_ import Money
from movie_ import Movie
from movie_type_ import MovieType
from period_condition_ import PeriodCondition
from screening_ import Screening
from sequence_condition_ import SquenceCondition

if __name__ == "__main__":
    sq_condition1 = SquenceCondition(1)
    sq_condition2 = SquenceCondition(2)
    period_condition1 = PeriodCondition(
        DAY_OF_WEEKS.get("Monday"), time(9, 00), time(19, 00)
    )
    period_condition2 = PeriodCondition(
        DAY_OF_WEEKS.get("Tuesday"), time(9, 00), time(19, 00)
    )
    the_batman = Movie(
        "the batman",
        Money.from_wons(18000),
        Money.from_wons(10000),
        0.1,
        MovieType.AMOUNT_DISCOUNT,
        [sq_condition1, sq_condition2],
        None,
    )
    screening = Screening(the_batman, 1, datetime(2022, 11, 14, 18, 30, 0))
    reservation = screening.reserve(Customer("steve", 101), 2)
    print(reservation)
