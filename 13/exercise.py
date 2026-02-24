COUNTRIES = [
    ("Canada", 100_000, 200_000),
    ("Mexico", 250, 300),
    ("Greenland", 790000123, 465778),
    ("Iceland", 80970, 567845),
]


def print_tuple(tup):
    formatter = "{0:15} {1:>12} {2:>15}"
    return formatter.format(*tup)


def print_tuples(tuples):
    header = ("Country", "GDP", "Population")
    print(print_tuple(header))
    print("=" * 44)
    for t in tuples:
        print(print_tuple(t))


print_tuples(COUNTRIES)
