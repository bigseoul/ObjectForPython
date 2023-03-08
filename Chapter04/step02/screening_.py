from datetime import datetime

from movie_ import Movie
from movie_type_ import MovieType


class Screening:

    # 자바처럼 디폴트 생성자를 만들어주지 않으니, 만드는데
    # None으로 해도 되나?
    # https://gongmeda.tistory.com/12

    def __init__(self, movie: Movie, sequence, when_Screened) -> None:
        self.__movie = movie
        self.__sequence = sequence
        self.__when_screened = when_Screened

    def calculate_fee(self, audience_count):
        if self.__movie.get_Movie_type() == MovieType.AMOUNT_DISCOUNT:
            if self.__movie.is_discountable(self.__when_screened, self.__sequence):
                return self.__movie.calculate_amount_discounted_fee().times(
                    audience_count
                )
        elif self.__movie.get_Movie_type() == MovieType.PERCENT_DISCOUNT:
            return self.__movie.calculate_percent_discounted_fee().times(audience_count)
        elif self.__movie.get_Movie_type() == MovieType.NONE_DISCOUNT:
            return self.__movie.calculate_none_discounted_fee(audience_count)
        else:
            return self.__movie.calculate_none_discounted_fee(audience_count)
