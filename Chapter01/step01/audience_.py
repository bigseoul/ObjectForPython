from bag_ import Bag


class Audience:
    """
    관램객은 소지품을 보관하기 위해 가방을 가질 수 있다
    """

    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    # Bag 자료형
    def get_bag(self) -> Bag:
        return self.__bag
