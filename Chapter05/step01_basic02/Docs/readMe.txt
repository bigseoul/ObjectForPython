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

=basic02=
*주요 도매인에 아는 것 추가-정보 관리 책임자가 알아야 하는 것
1. Screening: movie:Movie, squence:int, when_screened:datetime
2. Movie: title, fee, discount_amount, movie_type(할인정책): enum, discount_conditions: DiscountCondition(할인조건들)
3. 상수, DAY_OF_WEEK in Constant

*DiscountCondition 객체 추가
1. Movie가 DC에게 할인 조건이 있는지 물어봄. DC는 조건에 상영이 개별 조건에 만족하는 지 확인하고 알려 줌.
2. DC가 아는 것은 discount_type(조건 종류): enum, sequence(순번), day_of_week(요일), start_time(할인 시작 시간), end_time(할인 종료 시간)
3. DC가 아는 것과 상영시간(Screening)을 비교하기 위해선 Screening 객체를 넘겨 받아와야 함.
