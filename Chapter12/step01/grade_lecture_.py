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
        """
        1. scores 리스트에 있는 점수가
        2. grade 점수대 가운데 있는가?
        3. 점수대 마다 그리고 몇 개?
        chatGPT 미쳤네 ㅋㅋ
        """
        # scores = self.get_scores()
        # filtered_scores = list(filter(lambda x: grade.include(x), scores))
        # return len(filtered_scores)

        return len(list(filter(lambda x: grade.include(x), self.get_scores())))

    def average(self, grade_name: str) -> Optional[float]:
        """
        1. overloading in python?
        -lecture.average()는 받아들이지 않네.
        -오버로드를 허용하지 않는건가?

        2. 많은 분들을 혼란스럽게 하는 부분이 있는데요.
        filter() 함수는 filter 타입으로 결과를 리턴한다는 점입니다.
        filter() 함수의 결과값을 list로 변환하는 가장 쉬운 방법은
        list() 내장 함수를 사용하는 것입니다.
        https://www.daleseo.com/python-filter/
        //필터는 필터로 결과값을 내오기에, 이를 변화하는 과정이 필요.
        그래서 list를 이용해 값이 하나더라도 결과값 형식을 바꾸고,
        [0]번째에 담긴 값으로 데이터를 처리함.

        map 앞에 list 함수를 통해 list 자료형으로 바꾸는 이유는
        map 이 반환하는 것이 실제로는 list 자료형이 아니기 때문입니다.
        map 함수는 Iterator 를 반환하는데,
        이를 list로 변환해서 list 자료형으로 만드는 것입니다.
        """
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
