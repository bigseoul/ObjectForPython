from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer_ import Customer
    from money_ import Money
    from screening_ import Screening


class Reservation:
    """
    아는 것: 고객정보, 상영정보, 상영요금, 인원 수
    하는 것: 고객정보와 상영정보, 요금정보를 합쳐 예약 객체 생성.
    """

    def __init__(
        self,
        customer: "Customer",
        screening: "Screening",
        fee: "Money",
        audience_count: int,
    ) -> None:
        self.__customer = customer
        self.__screening = screening
        self.__fee = fee
        self.__audience_count = audience_count

    def __str__(self) -> str:
        return f"==예약기록==\n{self.__customer}\n{self.__screening}\n{self.__fee}\n관객수: {self.__audience_count}"
