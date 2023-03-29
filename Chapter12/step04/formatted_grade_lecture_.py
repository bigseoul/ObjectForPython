from grade_lecture_ import GradeLecture


class FormattedGradeLecture(GradeLecture):
    def __init__(self, title: str, success: int, grades: list, scores: list) -> None:
        super().__init__(title, success, grades, scores)

    def format_average(self):
        """이 예제도, 파이썬이 오버로드를 지원하지 않아 실험할 수 없음"""

        return f"Avg: {super().average():1.1f}"
