import random
import string


def create_password_generator(characters):
    def generator(n):
        return "".join(random.choices(characters, k=n))

    return generator


alpha_gen = create_password_generator(
    string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
)
weird_gen = create_password_generator(
    string.ascii_letters + string.digits + string.punctuation
)

print(alpha_gen(5))
print(alpha_gen(10))
print(weird_gen(4))
print(weird_gen(12))
