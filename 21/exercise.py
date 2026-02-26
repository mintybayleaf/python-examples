import fileinput


def longest_word_per_file():
    max_word_length = 0
    for line in fileinput.input():
        max_word_length = max(
            max_word_length, *[len(word) for word in line.rstrip().split(" ")]
        )

    return max_word_length


if __name__ == "__main__":
    print(longest_word_per_file())
