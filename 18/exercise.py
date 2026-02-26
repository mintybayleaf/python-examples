import sys


def last_line(stream):
    line = None
    for l in stream:
        line = l.rstrip()
    return line


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            print(last_line(file))
    else:
        print(last_line(sys.stdin))
