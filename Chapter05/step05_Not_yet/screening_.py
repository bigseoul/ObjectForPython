from datetime import datetime
from typing import TYPE_CHECKING

from money_ import Money
from reservation_ import Reservation

if TYPE_CHECKING:
    from customer_ import Customer
    from movie_ import AbsMovie


class Screening:
    def __init__(
        self, movie: "AbsMovie", sequence: int, when_screened: datetime
    ) -> None:
        self.__movie = movie
        self.__sequence = sequence  # Screening sequence
        self.__when_screened = when_screened  # Screening date

    def reserve(self, customer: "Customer", audience_count: int) -> Reservation:
        total_fee = self._calculate_fee(audience_count)
        return Reservation(self, customer, total_fee, audience_count)

    def _calculate_fee(self, audience_count: int) -> Money:
        return self.__movie.calculate_movie_fee(self) * audience_count

    def get_when_screened(self) -> datetime:
        return self.__when_screened

    def get_sequence(self) -> int:
        return self.__sequence
