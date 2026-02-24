import io
import sys


def ubbi_dubbi(word):
    buffer = io.StringIO()
    for letter in word:
        if letter in "aeiouAEIOU":
            buffer.write(f"ub{letter}")
        else:
            buffer.write(letter)
    return buffer.getvalue()


if __name__ == "__main__":
    print(ubbi_dubbi(sys.argv[1]))
