from typing import TYPE_CHECKING

from reservation_ import Reservation

if TYPE_CHECKING:
    from movie_ import Movie


class Screening:
    def __init__(self, movie: "Movie", squence) -> None:
        self.__movie = movie
        self.__sequence = squence

    def __str__(self) -> str:
        return f"{self.__movie}, {self.__sequence}"

    def reserve(self, customer: str, audience_count: int) -> Reservation:
        total_fee = self.__calculate_fee(audience_count)

        print("# 4. <<create>> 예약을 만들어라")
        return Reservation(self, customer, total_fee, audience_count)

    def __calculate_fee(self, audience_count):
        print("# 2. 가격을 계산하라")
        return self.__movie.calculate_movie_fee(audience_count)
