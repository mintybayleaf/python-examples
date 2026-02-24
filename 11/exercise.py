import operator

COUNTRIES = [
    {"name": "spain"},
    {"name": "columbia"},
    {"name": "canada"},
    {"name": "usa"},
    {"name": "france"},
    {"name": "mexico"},
    {"name": "yemen"},
    {"name": "russia"},
    {"name": "uzbekistan"},
    {"name": "egypt"},
]


def sort_map(m, keyfn):
    return sorted(m, key=keyfn)


print(sort_map(COUNTRIES, operator.itemgetter("name")))
