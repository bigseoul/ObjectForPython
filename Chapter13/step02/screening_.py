from typing import TYPE_CHECKING
from reservation_ import Reservation
from datetime import datetime

if TYPE_CHECKING:
    from movie_ import Movie
    from customer_ import Customer


class Screening:
    # Screening(godzilla_vs_kong, 1, date(2021, 4, 3)) 이거 데이트타임으로 가야겠는데?
    def __init__(self, movie: "Movie", sequence: int, when_screened: datetime) -> None:
        self.__moive = movie
        self.__sequence = sequence
        self.__when_screened = when_screened

    def check_screen(self):
        print("===screen===")
        print(self.__sequence, self.__when_screened)
        self.__moive.check_movie()

    def get_start_time(self):
        return self.__when_screened

    def is_sequence(self, sequence: int):
        return self.__sequence == sequence

    def get_movie_fee(self):
        return self.__moive.get_fee()

    """private, __calculate_fee에 메시지를 보내 요금을 계산"""
    # screening.reserve(Customer("tom", 123), 1)
    def reserve(self, customer: "Customer", audience_count: int):
        
        
        return Reservation(
            customer, self, self.__calculate_fee(audience_count), audience_count
        )

    """private: movie객체에게 영화값에서 할인금액 뺀 알려달라고 메세지 보냄. money가 리턴 객체"""

    def __calculate_fee(self, audience_count: int):
        return self.__moive.calculate_movie_fee(self).times(audience_count)

    def get_end_time(self):
        return self.__moive.get_end_time_from(self.__when_screened)
