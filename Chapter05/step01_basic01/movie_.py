class Movie:
    def __init__(
        self, title, fee, discount_amount=None, discount_conditions=None
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__discount_amount = discount_amount
        # from_Movie_**에서 args를 list()받아서 보내줌. 패킹할 필요 없음.
        self.__discount_conditions = discount_conditions

    def __str__(self) -> str:
        return f"{self.__title}, {self.__fee}, {self.__discount_amount}, {self.__discount_conditions}"

    def calculate_movie_fee(self, audience_count):
        print("# 3. 할인여부를 판단하라")
        if self.__is_discountable():
            return (self.__fee - self.__discount_amount) * audience_count
        else:
            return self.__fee * audience_count

    def __is_discountable(self) -> bool:
        if self.__discount_conditions == "DC_Amount":
            return True
        else:
            return False
