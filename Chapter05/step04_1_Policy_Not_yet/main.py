import logging

logging.basicConfig(level=logging.INFO)

from datetime import datetime, time
from constant_ import DAY_OF_WEEK

from screening_ import Screening
from sequence_condition_ import SquenceCondition
from period_condition_ import PeriodCondition
from customer_ import Customer
from money_ import Money
from amount_discount_movie_ import AmountDiscountMovie
from percent_discount_movie_ import PercentDiscountMovie
from none_discount_movie_ import NoneDiscountMovie

if __name__ == "__main__":

    """순번 조건, 1회차 대상"""   
    sq_condition1 = SquenceCondition(1)

    """기간 조건, 금요일, 8월 13일 17시~21시까지, 0은 nothing""" 
    period_condition1 = PeriodCondition(
        DAY_OF_WEEK.get("Monday"),
        time(9, 00),
        time(19, 00)
    )

    the_batman = AmountDiscountMovie(
        "the batman",
        time(1, 53),
        Money.wons(18000),
        Money.wons(10000),
        sq_condition1, 
        period_condition1
    )
    screening = Screening(the_batman, 1, datetime(2022, 11, 14, 18, 30, 0))

    the_batman2 = PercentDiscountMovie(
        "the batman",
        time(1, 53),
        Money.wons(18000),
        0.1,
        sq_condition1, 
        period_condition1
    )
    screening2 = Screening(the_batman2, 1, datetime(2022, 11, 14, 18, 30, 0))


    the_batman3 = NoneDiscountMovie(
        "the batman",
        time(1, 53),
        Money.wons(18000),
        sq_condition1, 
        period_condition1
    )  
    screening3 = Screening(the_batman3, 1, datetime(2022, 11, 14, 18, 30, 0))
    
    reservation = screening.reserve(Customer("steve", 101), 2)  # steve를 Cumster객체로 바꾸기
    reservation2 = screening2.reserve(Customer("dave", 102), 1)  # steve를 Cumster객체로 바꾸기
    reservation3 = screening3.reserve(Customer("miz", 103), 2)  # steve를 Cumster객체로 바꾸기

    print(reservation3)