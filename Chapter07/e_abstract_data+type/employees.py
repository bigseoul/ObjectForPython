from dataclasses import dataclass

"""
파이썬에서 구조체 쓰기
https://singo112ok.tistory.com/80
https://docs.python.org/ko/3/library/dataclasses.html

"""


@dataclass
class Employees:
    name: str
    base_pay: float
    hourly: bool
    time_card: int

    def calculate_pay(self, tax_rate):
        if self.hourly:
            return self.__calculate_hourly_pay(tax_rate)
        return self.__calculate_salaried_pay(tax_rate)

    def monthly_base_pay(self):
        if self.hourly:
            return 0
        return self.base_pay

    def __calculate_hourly_pay(self, tax_rate):
        return (self.base_pay * self.time_card) - (
            self.base_pay * self.time_card
        ) * tax_rate

    def __calculate_salaried_pay(self, tax_rate):
        return self.base_pay - (self.base_pay * tax_rate)


employees = [
    Employees("직원A", 400, False, 0),
    Employees("직원B", 300, False, 0),
    Employees("직원C", 250, False, 0),
    Employees("아르바이트D", 1, True, 120),
    Employees("아르바이트E", 1, True, 120),
    Employees("아르바이트F", 1, True, 120),
]


def main(operation, name=""):
    if operation == "pay":
        calculate_pay(name)
    elif operation == "base_pays":
        sum_of_base_pays()
    else:
        return


def calculate_pay(name):
    tax_rate = get_tax_rate()
    for each in employees:
        temp_each: "Employees" = each
        if temp_each.name == name:
            employee = temp_each
            break
    pay = employee.calculate_pay(tax_rate)
    print(describe_result(name, pay))


def get_tax_rate():
    return float(input("세율을 입력하세요: "))


def describe_result(name, pay):
    return f"이름: {name}, 급여: {pay}"


def sum_of_base_pays():
    result = 0
    for each in employees:
        temp_each: "Employees" = each
        result += temp_each.monthly_base_pay()
    print(result)


main(operation="base_pays")
main(operation="pay", name="아르바이트F")
