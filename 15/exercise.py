RAINFALL = {}


def rainfall():
    while True:
        city = input()

        if not city:
            break

        inches = input()

        if not inches.isdigit():
            break

        RAINFALL.setdefault(city, 0)
        RAINFALL[city] += int(inches)

    for city, inches in RAINFALL.items():
        print(f"{city}: {inches}")


if __name__ == "__main__":
    rainfall()
