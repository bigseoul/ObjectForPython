import logging

logging.basicConfig(level=logging.INFO)

from datetime import datetime, time
from constant_ import DAY_OF_WEEK

from screening_ import Screening

from movie_ import Movie
from movie_type_ import MovieType

# from discount_condition_ import DiscountCondition
# from discount_condition_type_ import DiscountConditionType
from sequence_condition_ import SquenceCondition
from period_condition_ import PeriodCondition

from customer_ import Customer
from money_ import Money


if __name__ == "__main__":

    """순번 조건, 1회차 대상"""
    # sq_condition = DiscountCondition(
    #     DiscountConditionType.SEQUENCE_DISCOUNT,
    #     1,
    # )
    
    sq_condition1 = SquenceCondition(1)

    """기간 조건, 금요일, 8월 13일 17시~21시까지, 0은 nothing"""
    # period_condition = DiscountCondition(
    #     DiscountConditionType.PERIOD_DISCOUNT,
    #     0,
    #     DAY_OF_WEEK.get("Monday"),
    #     time(9, 00),
    #     time(19, 00),
    # )
    
    period_condition1 = PeriodCondition(
        DAY_OF_WEEK.get("Monday"),
        time(9, 00),
        time(19, 00)
    )

    the_batman = Movie(
        "the batman",
        Money.wons(18000),
        Money.wons(10000),
        10,
        MovieType.AMOUNT_DISCOUNT,
        sq_condition1, 
        period_condition1
    )
    screening = Screening(the_batman, 1, datetime(2022, 11, 14, 18, 30, 0))

    logging.info("Req - main: sending a reserve message to Screening")
    reservation = screening.reserve(Customer("steve", 101), 2)  # steve를 Cumster객체로 바꾸기
    print(reservation)