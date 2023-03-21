from datetime import datetime, time

from amount_discount_policy_ import AmountDiscountPolicy
from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from money_ import Money
from movie_ import Movie
from non_discount_policy_ import NoneDiscountPolicy
from period_condition_ import PeriodCondition
from screening_ import Screening
from sequence_condition_ import SquenceCondition

if __name__ == "__main__":
    # nondisocunt 확인

    # 상영 정보 만들기
    # 1. 할인조건 생성. 순서(이거부턴 완성)와 기간방식 할인
    sq_condition1 = SquenceCondition(1)

    # 2. 할인정책 생성(합성: 할인조건)
    nc1 = NoneDiscountPolicy()
    adp1 = AmountDiscountPolicy(Money.from_wons(2500), sq_condition1)

    # 3. 영화 생성
    the_batman = Movie("the batman", time(1, 53), Money.from_wons(18000), nc1)
    squid_game = Movie("squid game", time(2, 0), Money.from_wons(15000), adp1)

    # 4. 상영 생성 (합성: 영화, 합성: 할인정책)
    screen_for_the_batman = Screening(the_batman, 1, datetime(2023, 3, 21, 18, 00, 00))
    screen_for_squid_game = Screening(squid_game, 1, datetime(2023, 3, 21, 18, 00, 00))
    # 예약 만들기
    # 5. 예약 시행. Screening_영화이름_Non.Rerserve(고객 정보, 인원 수)
    reservation_for_steve = screen_for_the_batman.reserve(Customer("steve", 101), 2)
    reservation_for_miz = screen_for_squid_game.reserve(Customer("miz", 102), 1)

    print(reservation_for_miz)
