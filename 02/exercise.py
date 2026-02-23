import sys
import functools


def msum(*args):
    return functools.reduce(lambda result, x: result + x, args, 0)


if __name__ == "__main__":
    numbers = map(int, sys.argv[1:])
    print("sum:", msum(*numbers))
