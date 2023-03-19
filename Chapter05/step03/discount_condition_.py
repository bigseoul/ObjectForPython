from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening


class AbsDiscountCondition(ABC):
    """
    해결방법 2. 다형성을 통해 분리

        Movie 입장에서는 사실 둘다 할인 여부를 판단하는 동일한 책임을 수행할 뿐이다.

        할인 가능 여부를 반환하기만 하면
        Movie는 객체가 sequenceCondition 인지 periodCondition 인지
        상관하지 않는다.Movie 입장에서
        sequenceCondition 과 periodCondition이
        동일한 책임을 수행한다는 것은 동일한 역할을 수행한다는 것을 의미한다.

        DiscountCondition의 경우에서 알 수 있듯이 객체의 타입에 따라 변하는 행동이 있다면 타입을 분리하고 변화하는 행동을 각 타입의 책임으로 할당해야 한다.

        GRASP 에서는 이를 POLYMORPHISM(다형성) 패턴이라 부른다.
        다형성 패턴은 객체의 타입을 검사해서 타입에 따라
        여러 대안들을 수행하는 조건적인 논리를 사용하지 말라고 경고한다.

        만약 새로운 할인 조건이 추가된다면 어떻게 될까?

        DiscountCondition 이라는 추상화가 구체적인 타입들을 캡슐화 하고 있는 상황이다.

        Movie의 관점에서 DiscountCondition 이라는 추상화가 구체적인 타입을 캡슐화 한다는 것은,
        새로운 DiscountCondition 타입을 추가해도 Movie는 어떠한 수정도 필요가 없다.

        이처럼 변경을 캡슐화 하도록 책임을 할당하는 것을 GRASP 에서는
        PROTECTED VARIATIONS(변경 보호) 패턴이라고 부른다.

        변화가 예상되는 지점을 식별하고, 그 주위에 안정된 인터페이스를 형성하도록 책임을 할당하다.

        변경 보호 패턴은 책임 할당의 관점에서 캡슐화를 설명한 것 이다.

        "설계에서 변하는 것이 무엇인지 고려하고 변하는 개념을 캡슐화 하라"[GOF94] 라는 객체지향의 격언은 본질을 잘 설명한다.
    """

    @abstractmethod
    def is_satisfied_by(self, screening: "Screening") -> bool:
        pass
