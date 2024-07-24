import string
import random

characters = list(string.ascii_letters + string.digits + "ëç!@#$%^&*()")


def generate_random_password():
    length = int(input("Shkruani gjatesine e fjalekalimit: "))

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


generate_random_password()
