import sys


def msum(*args):
    if not args:
        return

    import functools

    return functools.reduce(lambda result, x: result + x, args[1:], args[0])


if __name__ == "__main__":
    print(msum(sys.argv[1]))
