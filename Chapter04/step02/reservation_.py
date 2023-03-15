from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer_ import Customer
    from discount_condition_ import DiscountCondition
    from money_ import Money
    from screening_ import Screening


class Reservation:
    def __init__(
        self, customer: "Customer", screening: "Screening", fee: "Money", audience_count
    ) -> None:
        self.__customer = customer
        self.__screening = screening
        self.__fee = fee
        self.__audience_count = audience_count

    def __str__(self) -> str:
        return f"Reservation: {self.__customer}, {self.__screening}, {self.__fee}, {self.__audience_count}"

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def screening(self):
        return self.__screening

    @screening.setter
    def screening(self, screening):
        self.__screening = screening

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, fee):
        self.__fee = fee

    @property
    def audience_count(self):
        return self.__audience_count

    @audience_count.setter
    def audience_count(self, audience_count):
        self.__audience_count = audience_count
