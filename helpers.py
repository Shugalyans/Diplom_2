import random
import string
from data import URL,payload
import requests

#данный метод пока не нужен
def create_new_random_user_for_test():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    yield

    return payload

def new_user():
    #отправляем запрос на создание пользователя
    response = requests.post(f'{URL}auth/register', payload)

    if response.status_code == 200:
        print("Красавчик")
        credentials = response.text
        print(credentials)
    else:
        print("Пошел нахер")
    yield
    response = requests.post(f'{URL}auth/login', payload)
    if response.status_code == 200:
        print("Умница")
        token = response.json()['accessToken']
        user_id = response.json()['user']
        print(f'ЮзерID: {user_id}')
        print(f'ТОКЕН: {token}')
        response_delete = requests.delete(f'{URL}auth/user', data=user_id, headers={'Authorization': token})
        assert response_delete.status_code == 202
    else:
        print("Дурачок")

