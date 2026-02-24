import sys


def ssort(word):
    letters = list(word)
    end = len(letters)
    while end > 0:
        current, ahead = 0, 1
        while ahead < end:
            if letters[current] > letters[ahead]:
                temp = letters[current]
                letters[current] = letters[ahead]
                letters[ahead] = temp
            ahead += 1
            current += 1
        end -= 1
    return "".join(letters)


if __name__ == "__main__":
    print(ssort(sys.argv[1]))
