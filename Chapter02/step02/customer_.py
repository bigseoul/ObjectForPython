class Customer:
    def __init__(self, name: str, id: int) -> None:
        self.__name = name
        self.__id = id

    def __str__(self) -> str:
        return f"이름: {self.__name}\n아이디: {self.__id}"
