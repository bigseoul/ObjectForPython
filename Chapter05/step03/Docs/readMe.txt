[step03]
*문제
1. 무비가 시쿼스와 피리어드에 결합, 결도합도 증가 
2. 새로운 할인 조건 추가시, 이 할인 조건만을 위한 리스트와 메서드 만들어야 
-SeniorConditoins, __is_satisfied_by_senior()필요. 
3. 할인 조건 추가시, 무비 변경해야 함. 

*다형성을 통해 분리하기
1. 다형성 이용해 분리. 
- is_satisfied_by_sequence()/__is_satisfied_by_period() 둘 다 할인해준다는 역할은 같음.
- 역할을 공유해야 할 필요성이 있다면 추상클래스/ 없다면 인터페이스
- 파이썬은 다중 상속이 되므로 인터페이스가 없음. 추상으로 고고씽

2. 

[step02]
*P.151, DiscountCondition 응집도 문제점 파악
=>응집도 낮은 클래스는 아래와 같은 세가지 문제 가지고 있어

1. 하나 이상의 변경 이유 존재 
=> 변경 이유에 따라 클래스 분리
-is_satisfiedBy(), 새로운 할인 조건이 생기면 수정 필요
-__is_satisfied_by_sequence(), 순번 조건 변경시 수정 필요
-__is_satisfied_by_period(), 기간 조건 변경시 수정 필요

2. 인스턴스 변수 초기화 시점 다름 
=>함게 초기화 되는 속성 기준으로 코드 분리
-squence 초기화시, day_of_week, start_time, end_time은 초기화 안함. 
그 반대 마찬가지

3. 메서들이 인스턴스 변수를 사용하는 방식(그룹)에 따라 
=> 속성 그룹과 해당 그룹에 접근하는 메서드 그룹을 기준으로 코드 분리
-__is_satisfied_by_sequence는 squence를 사용
-__is_satisfied_by_period는 day_of_week, start_time, end_time사용. 

*타입 분리하기
1. DiscountCondition을 squenceCondition과 PeriodConditon으로 나누기 

[step01]
=feedBack=
1. 커뮤니케이션 다이어그램 그리고 데이터 값 넘겨보면서 협력을 만든다.
2. 클래스 다이어그램으로 아는 것과 행동을 서서히 구체화 한다. 처음부터 다 만들지 않음

=baic04=
클래스 다이어그램과 커뮤니케이션 다이어그램 그리기

=basic03=
*기타 도매인 연결
1. Customer, Money, 

*Money 객체 추가(main에서 검증해본다)
1. Screening/Movie의 메서드 가운데 돈 관련 리턴객체는 Money
2. 돈 관련 데이터형도 Money로 바꾼다(어차피 동적이나 힌트를 주도록 한다)
3. main에서 던져주는 객체도 변경

*Movie-Money 협력
1. __is_discountable가 true이면, 할인 정책에 맞게 할인 해준다.
2. 할인 정책은 Amount/Percent/NonDiscount
3. 할인 정책에 맞게 계산
4. 그 계산에 인원 수를 곱한다.
5. 최종 가격을 리턴해줌.

=basic02= 
//이쯤에서 대략 주고 받은 협력과 데이터가 정해져야 함.
//클래스 다이어그램이나 메시지 다이어그램 & 커뮤니케이션 다이어그램
*주요 도매인에 아는 것 추가-정보 관리 책임자가 알아야 하는 것
1. Screening: movie:Movie, squence:int, when_screened:datetime
2. Movie: title, fee, discount_amount, movie_type(할인정책): enum, discount_conditions: DiscountCondition(할인조건들)
3. 상수, DAY_OF_WEEK in Constant

*DiscountCondition 객체 추가
1. Movie가 DC에게 할인 조건이 있는지 물어봄. DC는 조건에 상영이 개별 조건에 만족하는 지 확인하고 알려 줌.
2. DC가 아는 것은 discount_type(조건 종류): enum, sequence(순번), day_of_week(요일), start_time(할인 시작 시간), end_time(할인 종료 시간)
3. DC가 아는 것과 상영시간(Screening)을 비교하기 위해선 Screening 객체를 넘겨 받아와야 함.


=basic01=
*주요 도매인 협력 관계 만들기- 돌아가는 구조만 만들기 (main/screening/movie)
1. main: sending a reserve message to Screening
2. Screening: sending a __calculate_fee() to Screening
3. Screening: sending a calculate_movie_fee() to Movie
4. Movie: sending a is_Discountable() in Movie
5. Screen: Create a Reservation

*주요 도매인만 협력 관계 구축
-main, screening, movie(discountCondition), reservation

*도메인이 아는 것 및 주고 받는 데이터는 최소한 또는 더미자료형
-더미: customer -> string