import random
import string


def new_user_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    domain = random.choice(['gmail.com', 'rambler.ru', 'yandex.ru'])
    email = f'{generate_random_string(5)}@{domain}'
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload
