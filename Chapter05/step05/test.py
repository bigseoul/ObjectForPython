from typing import Union
from enum import Enum

class MovieType(Enum):
    AMOUNT_DISCOUNT = 1
    PERCENT_DISCOUNT = 2
    NONE_DISCOUNT = 3

class Movie:
    def __init__(self, movie_type: MovieType):
        self.movie_type = movie_type

class Money:
    pass  # Your Money class implementation

class MyClass:
    # Your class implementation

    def calculate_discounted_fee(self, movie: Movie) -> Money:
        if movie.movie_type == MovieType.AMOUNT_DISCOUNT:
            return self.calculate_amount_discounted_fee(movie)
        elif movie.movie_type == MovieType.PERCENT_DISCOUNT:
            return self.calculate_percent_discounted_fee(movie)
        elif movie.movie_type == MovieType.NONE_DISCOUNT:
            return self.calculate_none_discounted_fee(movie)

        raise ValueError("Invalid movie type")

    def calculate_amount_discounted_fee(self, movie: Movie) -> Money:
        pass  # Your implementation

    def calculate_percent_discounted_fee(self, movie: Movie) -> Money:
        pass  # Your implementation

    def calculate_none_discounted_fee(self, movie: Movie) -> Money:
        pass  # Your implementation
