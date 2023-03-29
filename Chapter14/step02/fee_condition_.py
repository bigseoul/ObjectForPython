from abc import ABCMeta, abstractmethod
from date_time_interval_ import DateTimeInterval
from call_ import Call


class FeeCondition(metaclass=ABCMeta):
    @abstractmethod
    def find_time_interval(self, call: Call) -> list[DateTimeInterval]:
        ...
        
