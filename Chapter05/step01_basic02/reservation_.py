from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening


class Reservation:
    def __init__(
        self, screen: "Screening", name: str, total_fee: int, audience_count: int
    ) -> None:
        self.__screen = screen
        self.__name = name
        self.__total_fee = total_fee
        self.__audience_count = audience_count

    def __str__(self) -> str:
        return (
            f"Screen: {self.__screen}\n"
            f"Name: {self.__name}\n"
            f"Total Fee: {self.__total_fee}\n"
            f"Audience Count: {self.__audience_count}"
        )
