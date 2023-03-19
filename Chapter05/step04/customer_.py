class Customer:
    def __init__(self, name, id) -> None:
        self.__name = name
        self.__id = id

    def __str__(self) -> str:
        return f"{self.__name}, {self.__id}"
