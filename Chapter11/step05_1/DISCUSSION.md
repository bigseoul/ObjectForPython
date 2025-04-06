# 전화 요금 계산 시스템 설계 논의

## 1. 전체 구조
```mermaid
graph TD
    A[Phone] -->|has| B[Call]
    A -->|uses| C[RatePolicy]
    C <|--implements-- D[BasicRatePolicy]
    C <|--implements-- E[AdditionalRatePolicy]
    D <|--extends-- F[RegularPolicy]
    D <|--extends-- G[NightlyDiscountPolicy]
    E <|--extends-- H[TaxablePolicy]
    E <|--extends-- I[RateDiscountablePolicy]
```

## 2. 주요 클래스의 역할

### 2.1 기본 구성요소
- **Phone**: 통화 기록 관리 및 요금 계산 요청
- **Call**: 개별 통화 기록 (시작 시간, 종료 시간, 통화 시간 계산)
- **Money**: 금액 표현 및 연산

### 2.2 요금 정책 계층 구조
- **RatePolicy**: 요금 정책 최상위 추상 클래스
- **BasicRatePolicy**: 기본 요금 계산 알고리즘 제공
- **AdditionalRatePolicy**: 부가 요금 정책 구현을 위한 추상 클래스

## 3. 주요 설계 원칙 적용

### 3.1 다형성과 추상화
```python
class RatePolicy(metaclass=ABCMeta):
    @abstractmethod
    def calculate_fee(self, phone: "Phone") -> Money:
        ...

class Phone:
    def __init__(self, rate_policy: RatePolicy) -> None:
        self.__rate_policy = rate_policy
```

### 3.2 템플릿 메서드 패턴 (BasicRatePolicy)
```python
class BasicRatePolicy(RatePolicy):
    def calculate_fee(self, phone: "Phone") -> Money:
        result = MoneyZero.ZERO
        for call in phone.get_calls():
            result = result.plus(self._calculate_call_fee(call))
        return result

    @abstractmethod
    def _calculate_call_fee(self, call: Call) -> Money:
        ...
```

### 3.3 데코레이터 패턴 (AdditionalRatePolicy)
```python
class AdditionalRatePolicy(RatePolicy):
    def __init__(self, following: RatePolicy) -> None:
        self.__following = following

    def calculate_fee(self, phone: "Phone") -> Money:
        fee = self.__following.calculate_fee(phone)
        return self._after_calculated(fee)
```

## 4. 실제 사용 예시
```python
# 기본 요금제
phone1 = Phone(RegularPolicy(Money.wons(1000), time(0, 0, 10)))

# 기본 요금제 + 세금
phone2 = Phone(
    TaxablePolicy(0.1,
        RegularPolicy(Money.wons(1000), time(0, 0, 10))
    )
)

# 기본 요금제 + 세금 + 할인
phone3 = Phone(
    RateDiscountablePolicy(0.2,
        TaxablePolicy(0.1,
            RegularPolicy(Money.wons(1000), time(0, 0, 10))
        )
    )
)
```

## 5. 주요 설계 결정 및 장점

### 5.1 합성 사용 이유
1. **유연성**: 다양한 정책 조합 가능
2. **단일 책임**: 각 클래스가 하나의 책임만 가짐
3. **개방-폐쇄**: 새로운 정책 추가가 기존 코드 수정 없이 가능
4. **테스트 용이성**: 정책을 쉽게 교체할 수 있어 테스트 작성이 쉬움

### 5.2 상속 대신 합성을 선택한 이유
- 정책 조합의 유연성 확보
- 런타임에 정책 변경 가능
- 새로운 정책 추가가 용이
- 다중 상속의 복잡성 회피

## 6. 요금 계산 프로세스
1. Phone의 calculate_fee() 호출
2. RatePolicy 인터페이스를 통한 다형적 호출
3. BasicRatePolicy의 템플릿 메서드 실행
4. 구체적인 정책(RegularPolicy 등)의 계산 수행
5. 부가 정책이 있다면 순차적으로 적용

## 7. 핵심 원칙
- **단일 책임 원칙 (SRP)**: 각 클래스는 하나의 책임만 가짐
- **개방-폐쇄 원칙 (OCP)**: 확장에는 열려있고 수정에는 닫혀있음
- **리스코프 치환 원칙 (LSP)**: 하위 클래스는 상위 클래스를 대체할 수 있음
- **의존성 역전 원칙 (DIP)**: 구체화가 아닌 추상화에 의존