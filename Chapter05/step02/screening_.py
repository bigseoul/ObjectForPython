from datetime import datetime
from typing import TYPE_CHECKING

from money_ import Money
from reservation_ import Reservation

if TYPE_CHECKING:
    from movie_ import Movie


class Screening:
    def __init__(self, movie: "Movie", squence, when_screened: datetime) -> None:
        self.__movie = movie
        self.__sequence = squence  # 상영 순번
        self.__when_screened = when_screened  # 상영 일자

    def reserve(self, customer, audience_count) -> Reservation:
        # 1.영화에게 가격 계산받고나서 비용 저장, 인원수도 알려줌
        # 2. 예매 객체 만들기
        total_fee = self.__calculate_fee(audience_count)
        return Reservation(self, customer, total_fee, audience_count)

    def __calculate_fee(self, audience_count):
        return self.__movie.calculate_movie_fee(self) * audience_count

    def get_when_screened(self) -> datetime:
        return self.__when_screened

    def get_sequence(self) -> int:
        return self.__sequence
