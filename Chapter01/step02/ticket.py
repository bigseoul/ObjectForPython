class Ticket:

    """일단, fee를 인자로 받지 않고 5000원으로 고정"""

    def __init__(self) -> None:
        self.__fee = 5000

    def get_fee(self):
        return self.__fee
