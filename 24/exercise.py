import fileinput


def reverse_lines():
    lines = []
    for line in fileinput.input():
        lines.append(" ".join(reversed(line.rstrip().split(" "))))

    print("\n".join(lines))


if __name__ == "__main__":
    reverse_lines()
