employees = ["직원A", "직원B", "직원C"]
base_pays = [400, 300, 250]


def main(name):
    tax_rate = get_tax_rate()
    print("세율: ", tax_rate)
    pay = calculate_pay_for(name, tax_rate)
    print(pay)
    print(describe_result(name, pay))


def get_tax_rate():
    return float(input("세율을 입력하세요: "))


def calculate_pay_for(name, tax_rate):
    index = employees.index(name)
    base_pay = base_pays[index]
    return base_pay - (base_pay * tax_rate)


def describe_result(name, pay):
    """양식문자 리터럴"""
    return f"이름: {name}, 급여: {pay}"


main("직원A")
