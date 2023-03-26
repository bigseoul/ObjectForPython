employees = ["직원A", "직원B", "직원C", "아르바이트D", "아르바이트E", "아르바이트F"]
base_pays = [400, 300, 250, 1, 1, 1.5]
hourlys = [False, False, False, True, True, True]
timeCards = [0, 0, 0, 120, 120, 120]


def calculate_pay(name, tax_rate):
    if is_hourly(name):
        pay = calculate_hourly_pay_for(name, tax_rate)
    else:
        pay = calculate_pay_for(name, tax_rate)
    return pay


def is_hourly(name):
    return hourlys[employees.index(name)]


def calculate_hourly_pay_for(name, tax_rate):
    index = employees.index(name)
    base_pay = base_pays[index] * timeCards[index]
    return base_pay - (base_pay * tax_rate)


def calculate_pay_for(name, tax_rate):
    """??"""
    index = employees.index(name)
    base_pay = base_pays[index]
    return base_pay - (base_pay * tax_rate)


def sum_of_base_pays():
    result = 0
    for name in employees:
        if not is_hourly(name):
            result += base_pays[employees.index(name)]
    return result
