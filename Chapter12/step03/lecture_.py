import statistics


class Lecture:
    def __init__(self, title: str, success: int, scores: list) -> None:
        self.__title = title
        self.__success = success
        self.__scores = scores

    def average(self) -> float:
        return statistics.mean(self.__scores)

    def get_scores(self) -> tuple:
        return tuple(self.__scores)

    def evaluate(self) -> str:
        return f"Pass: {self.pass_count()}, Fail: {self.__fail_count()}"

    def pass_count(self) -> int:
        return len(list(filter(lambda x: x > self.__success, self.__scores)))

    def __fail_count(self) -> int:
        return len(self.__scores) - self.pass_count()

    def stats(self):
        return "Title: {0}, Evaluation Method: {1}".format(
            self.__title, self.get_evaluation_method()
        )

    def get_evaluation_method(self):
        return "Pass or Fail"

    