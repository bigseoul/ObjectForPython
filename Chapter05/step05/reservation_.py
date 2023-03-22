from typing import TYPE_CHECKING

from customer_ import Customer
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening


class Reservation:
    def __init__(
        self,
        customer: Customer,
        screen: "Screening",
        total_fee: Money,
        audience_count: int,
    ) -> None:
        self.__screen = screen
        self.__customer = customer
        self.__audience_count = audience_count
        self.__total_fee = total_fee

    def __str__(self) -> str:
        return (
            f"Screen: {self.__screen}\n"
            f"Customer: {self.__customer}\n"
            f"Total Fee: {self.__total_fee}\n"
            f"Audience Count: {self.__audience_count}"
        )
