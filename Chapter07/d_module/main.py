import employees as employees


def main(operation, name=""):
    if operation == "pay":
        calculate_pay(name)
    elif operation == "base_pays":
        sum_of_base_pays()
    else:
        return


def calculate_pay(name):
    tax_rate = get_tax_rate()
    pay = employees.calculate_pay(name, tax_rate)
    print(describe_result(name, pay))


def get_tax_rate():
    return float(input("세율을 입력하세요: "))


def describe_result(name, pay):
    return f"이름: {name}, 급여: {pay}"


def sum_of_base_pays():
    print(employees.sum_of_base_pays())


main(operation="base_pays")
main(operation="pay", name="아르바이트F")
