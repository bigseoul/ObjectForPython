from datetime import datetime, time

from constant_ import DAY_OF_WEEK
from discount_condition_ import DiscountCondition
from discount_condition_type_ import DiscountConditionType
from movie_ import Movie
from movie_type_ import MovieType
from screening_ import Screening


def main():
    # """순번 조건, 1회차 대상"""
    # Sequence discount condition, targeting 1st sequence
    sq_condition = DiscountCondition(
        DiscountConditionType.SEQUENCE_DISCOUNT,
        1,
    )

    # """기간 조건, 금요일, 17시~21시까지, 0(순번)은 nothing"""
    # Period discount condition, Monday, 9AM to 7PM, 0 (sequence) is nothing

    period_condition = DiscountCondition(
        DiscountConditionType.PERIOD_DISCOUNT,
        0,
        DAY_OF_WEEK.get("Monday"),
        time(9, 00),
        time(19, 00),
    )

    # """영화: 할인정책-Amount, 조건-기간/순번"""
    the_batman = Movie(
        "the batman",
        18000,
        10000,
        MovieType.AMOUNT_DISCOUNT,
        discount_conditions=[
            period_condition,
            sq_condition,
        ],
    )

    # """상영: 1회차 상영, 날짜&시간 """
    screening = Screening(the_batman, 1, datetime(2022, 3, 18, 18, 30, 0))

    print("1. main: sending a reserve message to Screening")
    reservation = screening.reserve("Steve", 2)
    print(reservation)


if __name__ == "__main__":
    main()
