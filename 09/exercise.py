import sys


def firstlast(sequence):
    return sequence[0:1] + sequence[-1:]


if __name__ == "__main__":
    print(firstlast(sys.argv[1]))
