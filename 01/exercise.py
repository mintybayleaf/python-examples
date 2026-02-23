import random

number = random.randint(0, 100)


def parse_guess(guess):
    if guess:
        try:
            return int(guess)
        except ValueError:
            return None


def guessing_game():
    while guess := parse_guess(input("Guess a random number:")):
        if guess == number:
            print("You did it!")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    guessing_game()
