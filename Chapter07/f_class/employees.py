class Employee:
    def __init__(self, name, base_pay) -> None:
        self.name = name
        self.base_pay = base_pay

    def calculate_pay(self, tax_rate):
        raise NotImplementedError

    def monthly_base_pay(self):
        raise NotImplementedError


class SalariedEmployee(Employee):
    def __init__(self, name, base_pay) -> None:
        super().__init__(name, base_pay)

    def calculate_pay(self, tax_rate):
        return self.base_pay - (self.base_pay * tax_rate)

    def monthly_base_pay(self):
        return self.base_pay


class HourlyEmployee(Employee):
    def __init__(self, name, base_pay, time_card) -> None:
        super().__init__(name, base_pay)
        self.time_card = time_card

    def calculate_pay(self, tax_rate):
        return (self.base_pay * self.time_card) - (
            self.base_pay * self.time_card
        ) * tax_rate

    def monthly_base_pay(self):
        return 0


employees = [
    SalariedEmployee("직원A", 400),
    SalariedEmployee("직원B", 300),
    SalariedEmployee("직원C", 250),
    HourlyEmployee("아르바이트D", 1, 120),
    HourlyEmployee("아르바이트E", 1, 120),
    HourlyEmployee("아르바이트F", 1, 120),
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
        temp_each: "Employee" = each
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
        temp_each: "Employee" = each
        result += temp_each.monthly_base_pay()
    print(result)


main(operation="base_pays")
main(operation="pay", name="아르바이트F")
