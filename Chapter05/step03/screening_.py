import logging

logging.basicConfig(level=logging.INFO)

from typing import TYPE_CHECKING
from reservation_ import Reservation
from datetime import datetime
from money_ import Money

if TYPE_CHECKING:
    from movie_ import Movie


"""
1. 영화를 예매할 책임을 가지고 있음.
2. 영화 객체 정보, 순서 정보를 가지고 있음
3. 예매 객체를 생성함.
"""


class Screening:
    def __init__(self, movie: "Movie", squence, when_screened: datetime) -> None:
        self.__movie = movie
        self.__sequence = squence  # 상영 순번
        self.__when_screened = when_screened  # 상영 일자

    def reserve(self, customer, audience_count) -> Reservation:
        # 1.영화에게 가격 계산받고나서 비용 저장, 인원수도 알려줌
        # 2. 예매 객체 만들기
        logging.info("req Screening: sending a __calculate_fee() to internal")
        logging.info("6. Screening: Create a Reservation")
        total_fee = self.__calculate_fee(audience_count)
        return Reservation(self, customer, total_fee, audience_count)

    def __calculate_fee(self, audience_count) -> Money:
        logging.info("req Screening: sending a calculate_movie_fee() to Movie")
        return self.__movie.calculate_movie_fee(
            self  # screen 자기자신
        )  # 마지막에 머니객체.times(audience_count)로 곱해주기

    def get_when_screened(self) -> datetime:
        return self.__when_screened

    def get_sequence(self) -> int:
        return self.__sequence
