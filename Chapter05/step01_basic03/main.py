import logging

logging.basicConfig(level=logging.INFO)

from datetime import datetime, time

from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from discount_condition_ import DiscountCondition
from discount_condition_type_ import DiscountConditionType
from money_ import Money
from movie_ import Movie
from movie_type_ import MovieType
from screening_ import Screening

if __name__ == "__main__":

    """순번 조건, 1회차 대상"""
    sq_condition = DiscountCondition(
        DiscountConditionType.SEQUENCE_DISCOUNT,
        1,
    )

    """기간 조건, 금요일, 8월 13일 17시~21시까지, 0은 nothing"""
    period_condition = DiscountCondition(
        DiscountConditionType.PERIOD_DISCOUNT,
        0,
        DAY_OF_WEEKS.get("Monday"),
        time(9, 00),
        time(19, 00),
    )

    the_batman = Movie(
        title="the batman",
        fee=Money.from_wons(18000),
        discount_amount=Money.from_wons(10000),
        discount_percent=0.1,
        movie_type=MovieType.AMOUNT_DISCOUNT,
        discount_conditions=[
            period_condition,
            sq_condition,
        ],
    )
    screening = Screening(the_batman, 1, datetime(2022, 3, 18, 18, 30, 0))

    logging.info("Req - main: sending a reserve message to Screening")
    reservation = screening.reserve(Customer("steve", 101), 2)  # steve를 Cumster객체로 바꾸기
    print(reservation)
