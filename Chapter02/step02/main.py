from datetime import datetime, time

from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from money_ import Money
from movie_ import Movie
from pricing.amount_discount_policy_ import AmountDiscountPolicy
from pricing.non_discount_policy_ import NonDiscountPolicy
from pricing.percent_discount_policy_ import PercentDiscountPolicy
from pricing.period_condition_ import PeriodCondition
from pricing.sequence_condition_ import SequenceCondition
from screening_ import Screening

if __name__ == "__main__":
    """SequenceCondition + AmountDiscountPolicy"""
    sc1 = SequenceCondition(1)
    sc2 = SequenceCondition(2)
    adp = AmountDiscountPolicy(Money.from_wons(10000), sc1, sc2)  # type: ignore

    """ 영화이름, 상영시간, 영화금액, 할인정책이 인자"""
    godzilla_vs_kong = Movie("고질라VS콩", time(1, 53), Money.from_wons(18000), adp)
    screening = Screening(godzilla_vs_kong, 1, datetime(2022, 8, 3))

    # 1. 스크린에게 예약하라는 메시지를 보냄
    reservation = screening.reserve(Customer("tom", 123), 1)
    print(reservation)

    """PeriodCondition 8월 27일 토 + PercentDiscountPolicy"""
    pc1 = PeriodCondition(DAY_OF_WEEKS.get("Saturday"), time(9, 00), time(13, 00))
    pdp = PercentDiscountPolicy(0.1, pc1)  # type: ignore
    the_book_of_fish = Movie("자산어보", time(2, 6), Money.from_wons(12000), pdp)
    screening2 = Screening(the_book_of_fish, 3, datetime(2022, 8, 27, 11, 50, 00))

    reservation2 = screening2.reserve(Customer("daegyung", 124), 2)
    print(reservation2)

    """ NonDiscountPolicy"""
    star_wars = Movie(
        "Star Was", time(3, 30), Money.from_wons(10000), NonDiscountPolicy()
    )

    """
    합성을 통한 정책 변경. 
    5장(Chapter05 step04)은 할인 정책을 변경할 수 없음.
    할인 정책을 구현하기 위해 상속을 이용하고 있기 때문. 

    5장처럼 movie에 상속된게 아니라, 2장처럼 정책만 따로 분리한 뒤 Movie에 합성 시키면 됨.  
    합성이란 객체의 인자로 들어가는 것.
    상속은 부모를 서브타이핑한 것??? 
    
    """
    # star_wars.change_discount_policy(PercentDiscountPolicy(0.1, pc1))
    screening3 = Screening(star_wars, 1, datetime(2022, 8, 28, 11, 50, 00))

    reservation3 = screening3.reserve(Customer("Tohee", 125), 1)

    print(reservation3)
