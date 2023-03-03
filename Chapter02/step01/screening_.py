from datetime import datetime
from typing import TYPE_CHECKING

from money_ import Money
from reservation_ import Reservation

if TYPE_CHECKING:
    from customer_ import Customer
    from movie_ import Movie


class Screening:
    """
    상영: 영화와 그 시간, 가격 정보를 가진 오브젝트

    """

    def __init__(self, movie: "Movie", sequence: int, when_screened: datetime) -> None:
        self.__moive = movie
        self.__sequence = sequence
        self.__when_screened = when_screened

    def __str__(self) -> str:
        return f"순서: {self.__sequence}\n상영시간: {self.__when_screened}\n{self.__moive}"

    def get_start_time(self) -> datetime:
        return self.__when_screened

    def is_sequence(self, sequence: int) -> int:
        return self.__sequence == sequence

    def get_movie_fee(self) -> Money:
        return self.__moive.get_fee()

    def reserve(self, customer: "Customer", audience_count: int) -> Reservation:
        """
        private
        """
        return Reservation(
            customer, self, self.__calculate_fee(audience_count), audience_count
        )

    def __calculate_fee(self, audience_count: int) -> Money:
        """
        movie의 calculate_movie_fee의 반환값은 1인당 예매 요금.
        이 반환값에 인원 수 곱함.
        """
        return self.__moive.calculate_movie_fee(self).times(audience_count)
