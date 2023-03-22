from discount_policy_ import DiscountPolicy
from money_ import Money


class Movie:
    def __init__(
        self,
        title,
        running_time,
        fee: Money,
        discount_policy: DiscountPolicy,
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__running_time = running_time
        self.__discount_policy = discount_policy

    def calculate_movie_fee(self, screening) -> Money:
        # discountP에게서 할인된 요금 받아와서, 영화요금에서 뺀다.
        temp = self.__fee - self.__discount_policy.calculate_discount_amount(screening)
        return temp

    def get_fee(self) -> Money:
        return self.__fee

    def change_discount_policy(self, discount_policy: "DiscountPolicy"):
        """5장 164쪽, 정책 변경"""
        self.__discount_policy = discount_policy
