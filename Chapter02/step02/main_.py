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

from pricing.period_condition_ import PeriodCondition
from pricing.sequence_condition_ import SequenceCondition

if __name__ == "__main__":

    """추상클래스를 이용한 합성 사용하기"""
    """SequenceCondition + AmountDiscountPolicy"""
    sc1 = SequenceCondition(1)
    sc2 = SequenceCondition(2)
    # 1, 2회차 사람에겐 10000원을 할인해 줘라.
    adp = AmountDiscountPolicy(Money.wons(10000), sc1, sc2)

    """ 영화이름, 상영시간, 영화금액, 할인정책이 인자"""
    godzilla_vs_kong = Movie("고질라VS콩", time(1, 53), Money.wons(18000), adp)

    """실행시간에 할인 조건을 변경할 경우, 10%할인 됨. """
    # godzilla_vs_kong.change_discount_policy(PercentDiscountPolicy(0.1))

    screening = Screening(godzilla_vs_kong, 1, datetime(2022, 8, 3))
    reservation = screening.reserve(Customer("tom", 123), 1)
    reservation.check_reservation()

    """PeriodCondition 8월 27일 토 + PercentDiscountPolicy"""
    pc1 = PeriodCondition(DAY_OF_WEEK.get("Saturday"), time(9, 00), time(13, 00))
    # 수요일, 9시에서 13시에 영화를 보는 사람에게 할인 해줘라
    pdp = PercentDiscountPolicy(0.1, pc1)

    the_book_of_fish = Movie("자산어보", time(2, 6), Money.wons(12000), pdp)
    screening2 = Screening(the_book_of_fish, 3, datetime(2022, 8, 27, 11, 50, 00))
    reservation2 = screening2.reserve(Customer("daegyung", 124), 2)
    reservation2.check_reservation()

    """ NonDiscountPolicy"""
    star_wars = Movie("Star Was", time(3, 30), Money.wons(10000), NonDiscountPolicy())
    screening3 = Screening(star_wars, 0, datetime(2022, 8, 28, 11, 50, 00))
    reservation3 = screening3.reserve(Customer("Tohee", 125), 1)
    reservation3.check_reservation()
