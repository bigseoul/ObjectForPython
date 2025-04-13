각 챕터별로 구현된 주요 디자인 패턴들은 다음과 같습니다:

1. Chapter 01 (Theater 예제)
- **캡슐화(Encapsulation)** 패턴
- 객체들 간의 의존성을 낮추고 자율성을 높이는 방식으로 리팩토링
- Theater, TicketSeller, Audience 등의 객체들이 각자의 책임을 캡슐화

2. Chapter 02 (Movie 예제)
- **Template Method** 패턴
  - `AbsDiscountPolicy` 클래스에서 구현
  - 부모 클래스에 기본적인 알고리즘 흐름을 구현하고 중간에 필요한 처리를 자식 클래스에게 위임

3. Chapter 04-05 (Movie 예제 개선)
- **GRASP 패턴들**:
  - **Polymorphism(다형성)** 패턴: 타입에 따라 변하는 행동을 각 타입의 책임으로 할당
  - **Protected Variations(변경 보호)** 패턴: 변화가 예상되는 지점을 식별하고 안정된 인터페이스를 형성

4. Chapter 11 (전화 요금 계산 시스템)
- **Decorator** 패턴
  - `AdditionalRatePolicy`를 통한 요금 정책 조합
- **Strategy** 패턴
  - 다양한 요금 정책(`RatePolicy`)을 구현하는데 사용

5. Chapter 13
- **Contract(계약에 의한 설계)** 패턴
  - 사전조건(`_check_precondition`)과 사후조건(`_check_postcondition`)을 통한 메서드 계약 구현
