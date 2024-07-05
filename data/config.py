# config.py

from utils.utils import generate_random_user


class Config:
    user = generate_random_user()
    USER_CREATED = False
    USERNAME = user
    PASSWORD = "password123"
