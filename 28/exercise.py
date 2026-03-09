def integer_string(*numbers):
    return ",".join(str(number) for number in numbers)


print(integer_string(1, 2, 3, 4, 5, 6))
