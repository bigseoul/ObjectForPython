from statistics import mean
from lecture_ import Lecture
from grade_ import Grade

"""
https://www.daleseo.com/python-typing/
about optional
"""
from typing import Optional


class GradeLecture(Lecture):
    def __init__(self, title: str, success: int, grades: list, scores: list) -> None:
        super().__init__(title, success, scores)
        self.__grades = grades

    # Override
    def evaluate(self) -> str:
        return super().evaluate() + ", " + self.gradesStatistics()

    def gradesStatistics(self) -> str:
        formatted_grades = list(map(lambda x: self.re_format(x), self.__grades))
        result = " ".join(formatted_grades)
        return result

    def re_format(self, grade: Grade):
        return f"{grade.name}:{self.grade_count(grade)}"

    def grade_count(self, grade: Grade):
        return len(list(filter(lambda x: grade.include(x), self.get_scores())))

    
    def average(self, grade_name: str) -> Optional[float]:

        filtered_grades = list(
            filter(lambda each: each.is_name(grade_name), self.__grades)
        )
        if filtered_grades:
            return self.grade_average(filtered_grades[0])
        else:
            return None

    def grade_average(self, grade: Grade) -> float:
        """
        filter(조건 함수, 순회 가능한 데이터)
        # scores = list(filter(grade.include, self.get_scores()))
        람다 안쓰고도 위처럼 할 수 있음.
        """
        scores = list(filter(lambda x: grade.include(x), self.get_scores()))
        result = mean(scores) if scores else 0
        return result
