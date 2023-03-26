employees = ["직원A", "직원B", "직원C"]
base_pays = [400, 300, 250]


def main(operation, name=""):
    if operation == "base_pays":
        sum_of_base_pays()
    elif operation == "pay":
        calculate_pay(name)
    else:
        return


def calculate_pay(name):
    tax_rate = get_tax_rate()
    print("세율: ", tax_rate)
    pay = calculate_pay_for(name, tax_rate)
    print(describe_result(name, pay))


def get_tax_rate():
    return float(input("세율을 입력하세요: "))


def calculate_pay_for(name, tax_rate):
    index = employees.index(name)
    base_pay = base_pays[index]
    return base_pay - (base_pay * tax_rate)


def describe_result(name, pay):
    return f"이름: {name}, 급여: {pay}"


def sum_of_base_pays():
    result = 0
    for base_pay in base_pays:
        result += base_pay
    print("총 기본급: ", result)


main(operation="base_pays")
main(operation="pay", name="직원A")
