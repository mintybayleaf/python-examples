import string


def gematria_dict():
    return dict(zip(string.ascii_lowercase, range(1, 27)))


GEMATRIA_DICT = gematria_dict()


def gematria_word(word):
    return sum(
        GEMATRIA_DICT[letter]
        for letter in word.lower()
        if letter in GEMATRIA_DICT.keys()
    )


def gematria_equal_words(word):
    score = gematria_word(word)
    words = []
    with open("/usr/share/dict/words", "r") as file:
        for line in file:
            w = line.rstrip()
            nscore = gematria_word(w)
            if nscore == score:
                words.append(w)
        return words


print(gematria_equal_words("cat"))
