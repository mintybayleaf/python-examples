import fileinput


def file_counts():
    words = []
    lines = 0
    for line in fileinput.input():
        words.extend(word for word in line.rstrip().split(" "))
        lines += 1

    return {
        "lines": lines,
        "words": len(words),
        "characters": sum(map(len, words)),
        "unique_words": len(set(words)),
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(file_counts(), indent=4)
