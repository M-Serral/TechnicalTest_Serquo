import random
import string


def generate_random_user():
    characters = string.ascii_letters + string.digits
    user = ''.join(random.choice(characters) for _ in range(10))
    return user

