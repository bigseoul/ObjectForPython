from datetime import datetime
from typing import TYPE_CHECKING

from money_ import Money
from movie_ import Movie
from reservation_ import Reservation

if TYPE_CHECKING:
    from customer_ import Customer


class Screening:
    def __init__(self, movie: Movie, sequence: int, when_screened: datetime) -> None:
        self.__movie = movie
        self.__sequence = sequence  # Screening sequence
        self.__when_screened = when_screened  # Screening date

    def reserve(self, customer: "Customer", audience_count: int) -> Reservation:
        total_fee = self._calculate_fee(audience_count)
        return Reservation(customer, self, total_fee, audience_count)

    def _calculate_fee(self, audience_count: int) -> Money:
        # screeing객체를 movie에 던저줌. 영화 요금 받아오면 인원 수 곱함.
        return self.__movie.calculate_movie_fee(self) * audience_count

    def get_when_screened(self) -> datetime:
        return self.__when_screened

    def get_sequence(self) -> int:
        return self.__sequence
