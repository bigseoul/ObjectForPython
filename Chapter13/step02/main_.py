import logging
from datetime import date, time, datetime

from constant_ import DAY_OF_WEEK
from customer_ import Customer
from money_ import Money
from movie_ import Movie
from screening_ import Screening

from pricing.amount_discount_policy_ import AmountDiscountPolicy
from pricing.percent_discount_policy_ import PercentDiscountPolicy
from pricing.non_discount_policy_ import NonDiscountPolicy
from pricing.broken_discount_policy_ import BrokenDiscountPolicy

from pricing.period_condition_ import PeriodCondition
from pricing.sequence_condition_ import SequenceCondition

if __name__ == "__main__":

    period_con = PeriodCondition(DAY_OF_WEEK.get("Saturday"), time(9, 00), time(13, 00))
    seq_con = SequenceCondition(1)

    bdp = BrokenDiscountPolicy(period_con, seq_con)

    the_book_of_fish = Movie("자산어보", time(2, 6), Money.wons(12000), bdp)
    the_book_of_fish2 = Movie("자산어보", time(2, 6), Money.wons(500), bdp)

    # 자정이 넘은 새벽 1시 __check_stronger_precondition
    # screening = Screening(the_book_of_fish, 3, datetime(2023, 2, 18, 1, 00, 00))
    # reservation = screening.reserve(Customer("daegyung", 124), 2)
    # reservation.check_reservation()

    # 영화 가격 1000원 __check_stronger_postcondition
    screening2 = Screening(the_book_of_fish2, 3, datetime(2023, 2, 18, 1, 00, 00))
    reservation2 = screening2.reserve(Customer("daegyung", 124), 2)
    reservation2.check_reservation()
