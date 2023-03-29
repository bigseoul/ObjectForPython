class InvalidScreeningException(RuntimeError):
    def __init__(self) -> None:
        super().__init__("screening의 사전조건 만족 못함.")
