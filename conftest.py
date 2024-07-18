import pytest

from data import URL, payload
import requests
from endpoints.users import User

@pytest.fixture()
def make_new_user():
    response = requests.post(f'{URL}auth/register', payload)
    token = response.json()['accessToken']
    yield response
    response = requests.delete(f'{URL}auth/user', headers={'Authorization': token})
