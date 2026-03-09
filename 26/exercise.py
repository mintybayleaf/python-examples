import functools
import operator


def prefix(op, *numbers):
    match op:
        case "+":
            return functools.reduce(operator.add, numbers, 0)
        case "-":
            return functools.reduce(operator.sub, numbers, 0)
        case "*":
            return functools.reduce(operator.mul, numbers)
        case "/":
            return functools.reduce(operator.floordiv, numbers)
        case "%":
            return functools.reduce(operator.mod, numbers)
        case "**":
            return functools.reduce(lambda x, y: x**y, numbers)
        case _:
            raise RuntimeError(f"operator {op} not supported")


print(prefix("+", 1, 2, 3, 4, 5))
print(prefix("-", 1, 2, 3, 4, 5))
print(prefix("*", 1, 2, 3, 4, 5))
print(prefix("/", 50, 5, 2))
print(prefix("**", 2, 2, 2))
print(prefix("%", 50, 6, 3))
