import sys

VOWELS = 'aeiouAEIOU'

def pig_latin(word):
    if word:
        if word[0] in VOWELS:
            return word + 'way'
        else:
            return word[1:] + word[0] + 'ay'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(pig_latin(sys.argv[1]))



