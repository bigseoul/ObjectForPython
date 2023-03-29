a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = "str"
success = 5
result = list(map(lambda x: str(x) if x % 3 == 0 else x, a))

result2 = list(filter(lambda x: x > success, a))
temp = " ".join(b)
print(temp)
