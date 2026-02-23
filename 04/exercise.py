import sys

BASE16 = "0123456789ABCDEF"


def parse_num(number):
    if number:
        try:
            return int(number)
        except ValueError:
            return 0


def convert(number):
    characters = []
    while number > 0:
        remainder = number % 16
        number = number // 16
        characters.append(BASE16[remainder])
    else:
        characters.append("0")

    return "".join(reversed(characters))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(convert(parse_num(sys.argv[1])))
    else:
        print("invalid number")
