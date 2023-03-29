class Grade:
    def __init__(self, name: str, upper: int, lower: int) -> None:
        self.__name = name
        self.__upper = upper
        self.__lower = lower

    @property
    def name(self) -> str:
        return self.__name

    def is_name(self, name) -> bool:
        return self.__name == name

    def include(self, score) -> bool:
        return score >= self.__lower and score <= self.__upper


