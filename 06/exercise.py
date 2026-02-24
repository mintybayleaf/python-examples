import sys


def to_pig(word):
    if word[0] in 'aeiouAEIOU':
        return word + 'way'

    return word[1:] + word[0] + 'ay'


def pig_latin_sentence(sentence):
    words = sentence.split(' ')
    return ' '.join(to_pig(word) for word in words)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(pig_latin_sentence(sys.argv[1]))
