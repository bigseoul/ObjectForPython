from datetime import datetime, time
from fee_condition_ import FeeCondition
from date_time_interval_ import DateTimeInterval
from call_ import Call


class TimeOfDayFeeCondition(FeeCondition):
    """
    시간대별 정책
    1. 적용 시작 시각 __from_time
    2. 적용 종료 시각 __to_time
    """

    def __init__(self, from_time: time, to_time: time) -> None:
        self.__from_time = from_time
        self.__to_time = to_time

    def find_time_interval(self, call: Call) -> list[DateTimeInterval]:
        intervals = call.get_interval().split_by_day()
        result = []

        for interval in intervals:
            """요금 조건에 맞게 call 인터발을 다시 만듦."""
            """__cmp_from_time < __cmp_to_time 하는 이유는 엉뚱한 값 들어가나? 무슨 이유로?"""

            if self.__cmp_from_time(interval) < self.__cmp_to_time(interval):
                result.append(
                    DateTimeInterval.from_combine(
                        datetime.combine(
                            interval.from_time.date(), self.__cmp_from_time(interval)
                        ),
                        datetime.combine(
                            interval.to_time.date(), self.__cmp_to_time(interval)
                        ),
                    )
                )
        return result

    def __cmp_from_time(self, interval: DateTimeInterval) -> time:
        """
        '인터벌 시작 시각'이 '적용 시작 시각'보다
        전이면, 적용 시작 시각 리턴

        후이면, '인터벌 시작 시각' 리턴

        CASE1)
        인터벌 시각 17~19시
        적용 시각 18~20시 //저녁할인?
        리턴: 18시 리턴(적용 시작 시각)

        CASE2) 인터벌 시각 19~20시
        적용 시각 18~20시 //저녁할인?
        리턴: 19시 리턴(인터벌 시작 시각)

        '인터벌 시작 시각'이 '적용 시작 시각'보다
        전이면, '적용 시작 시각' 리턴 //18시

        """
        if interval.from_time.time() < self.__from_time:
            print("__from_time: ", self.__from_time)
            return self.__from_time
        else:
            print("interval.from_time.time(): ", interval.from_time.time())
            return interval.from_time.time()
        # return (
        #     self.__from_time
        #     if (interval.from_time.time() < self.__from_time)
        #     else interval.from_time.time()
        # )

    def __cmp_to_time(self, interval: DateTimeInterval) -> time:
        """
        '인터벌 끝 시각'이 '적용 끝 시각'보다
        후면, '적용 끝 시각' 리턴

        앞이면, '인터벌 종료 시각' 리턴

        CASE1)
        인터벌 시각 17~19시
        적용 시각 18~20시 //저녁할인?
        리턴: 19시 리턴(인터벌 종료 시각)

        CASE2) 인터벌 시각 19~21시
        적용 시각 18~20시
        리턴: 20시 리턴(적용 종료 시각)

        """
        if interval.to_time.time() > self.__to_time:
            print("__to_time: ", self.__to_time)
            return self.__to_time
        else:
            print("interval.to_time.time():", interval.to_time.time())
            return interval.to_time.time()
        # return (
        #     self.__to_time
        #     if (interval.to_time.time() > self.__to_time)
        #     else interval.to_time.time()
        # )
