from datetime import date, time, datetime
from constant_ import DAY_OF_WEEK
from customer_ import Customer
from discount_condition_ import DiscountCondition
from discount_condition_type_ import DiscountConditionType
from movie_ import Movie
from money_ import Money
from movie_type_ import MovieType
from reservation_ import Reservation
from reservation_agency_ import ReservationAgency
from screening_ import Screening

if __name__ == "__main__":
    # dc = DiscountCondition()
    # dc.type = DiscountConditionType.PERIOD
    # dc.day_of_week = DAY_OF_WEEK.get("Friday")
    # dc.start_time = datetime(2021, 8, 13, 17, 0, 0)
    # dc.end_time = datetime(2021, 8, 13, 21, 0, 0)

    # movie객체에서 생성자 오버로드 여러 개 해줘야 함.
    # @classmethod 데코레이터 이용함.
    # 각 생성자에 맞는 클래스메서드명 붙이기
    # free_guy = Movie.from_Movie_for_non_discount("Free guy", time(1, 55), 10000)
    # free_guy = Movie.from_Movie_for_discount_amount(
    #     "free guy", time(1, 55), Money.wons(14000), Money.wons(5000), dc
    # )

    # setter/getter 이렇게 해도 되는군아. Screening __init__에 받는 movie, seq, when 인자 없음.
    # screening = Screening()
    # screening.movie = free_guy
    # screening.sequence = 1
    # screening.when_screened = datetime(2021, 8, 13, 18, 30, 0)

    # reservation = ReservationAgency.reserve(screening, Customer("bigseoul", "0001"), 1)
    # print("Movie.fee=", free_guy.fee.check_amount())
    # print("Reservation.fee=", reservation.fee.check_amount())
