from lecture_ import Lecture
from grade_lecture_ import GradeLecture
from grade_ import Grade
from professor_ import Professor

if __name__ == "__main__":
    professor = Professor(
        "다익스트라",
        GradeLecture(
            "객체지향 프로그래밍",
            70,
            [
                Grade("A", 100, 95),
                Grade("B", 94, 80),
                Grade("C", 79, 70),
                Grade("D", 69, 50),
                Grade("F", 49, 0),
            ],
            [81, 95, 97, 50, 45],
        ),
    )

    """
    파이썬은 상속 오버로딩과 그냥 오버로딩 둘 다 안됨.
    클래스 메서드 쓰는 것은 다형성 이용과 관계없음.
    오버로딩이 안되는 이유는, 
    XXX_method(a:int, b:float)와 XXX_method(a:list, b:float)를 구분할 수 없기 때문
    코더는 타입힌트로 구분할 수 있으나, 동적타입인 파이선 인터프리터는 구분할 수 없음.
    따라서 오버로드를 아예 막아버림.   
    """
    # print(professor.compile_statistics())
    # GradeLecture.average() missing 1 required positional argument: 'grade_name'

    print(professor.compile_statistics("A"))
    # [다익스트라] Pass: 3, Fail: 2, A:2 B:1 C:0 D:1 F:1, 96.0
