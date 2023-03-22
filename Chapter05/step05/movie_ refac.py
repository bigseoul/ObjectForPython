from datetime import time
from typing import TYPE_CHECKING

from discount_condition_type_ import DiscountConditionType
from movie_type_ import MovieType

if TYPE_CHECKING:
    from money_ import Money


class Movie:
    def __init__(
        self,
        movie_type,
        title,
        running_time,
        fee=None,
        discount_amount=None,
        discount_percent=None,
        discount_conditions=None,
    ):
        self.movie_type = movie_type
        self.title = title
        self.running_time = running_time
        self.fee = fee
        self.discount_amount = discount_amount
        self.discount_percent = discount_percent
        self.discount_conditions = discount_conditions

    @classmethod
    def from_movie_for_discount_percent(cls, title, running_time, fee, discount_percent, *discount_conditions):
        return cls(
            movie_type="percent_discount",
            title=title,
            running_time=running_time,
            fee=fee,
            discount_percent=discount_percent,
            discount_conditions=list(discount_conditions),
        )

    @classmethod
    def from_movie_for_discount_amount(cls, title, running_time, fee, discount_amount, *discount_conditions):
        return cls(
            movie_type="amount_discount",
            title=title,
            running_time=running_time,
            fee=fee,
            discount_amount=discount_amount,
            discount_conditions=list(discount_conditions),
        )

    @classmethod
    def from_movie_for_non_discount(cls, title, running_time, fee):
        return cls(
            movie_type="none_discount",
            title=title,
            running_time=running_time,
            fee=fee,
        )

    @property
    def movie_type(self):
        return self.__movie_type

    @movie_type.setter
    def movie_type(self, movie_type):
        self.__movie_type = movie_type

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, fee):
        self.__fee = fee

    @property
    def discount_conditions(self):
        return self.__discount_conditions

    @discount_conditions.setter
    def discount_conditions(self, *discount_conditions):
        self.__discount_conditions = list(discount_conditions)

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self.__discount_amount = discount_amount

    @property
    def discount_percent(self):
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        self.__discount_percent = discount_percent
