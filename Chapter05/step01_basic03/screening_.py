from datetime import datetime
from typing import TYPE_CHECKING

from reservation_ import Reservation

if TYPE_CHECKING:
    from movie_ import Movie


class Screening:
    """
    1. 영화를 예매할 책임을 가지고 있음.
    2. 영화 객체 정보, 순서 정보를 가지고 있음
    3. 예매 객체를 생성함.
    """

    def __init__(self, movie: "Movie", squence: int, when_screened: datetime) -> None:
        self.__movie = movie
        self.__sequence = squence  # 상영 순번
        self.__when_screened = when_screened  # 상영 일자

    def __str__(self) -> str:
        return (
            f"Movie: {self.__movie}\n"
            f"Sequence: {self.__sequence}\n"
            f"Screening Date: {self.__when_screened}"
        )

    def reserve(self, customer, audience_count):
        # 1.영화에게 가격 계산받고나서 비용 저장, 인원수도 알려줌
        # 2. 예매 객체 만들기
        print("2. screen: sending a __calculate_fee() to internal")
        total_fee = self.__calculate_fee(audience_count)
        print("5. Screen: Create a Reservation")
        return Reservation(self, customer, total_fee, audience_count)

    def __calculate_fee(self, audience_count):
        print("3. screen: sending a calculate_movie_fee() to Movie")
        return self.__movie.calculate_movie_fee(self) * audience_count  # screen 자기자신

    def get_when_screened(self):
        return self.__when_screened

    def get_sequence(self):
        return self.__sequence
