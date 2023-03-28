from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer_ import Customer
    from screening_ import Screening
    from money_ import Money


class Reservation:
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

    def check_reservation(self):
        print("===reservation===")
        self.__customer.check_customer()
        self.__screening.check_screen()
        self.__fee.check_amount()  
        print("===audience_count===")
        print(self.__audience_count)
