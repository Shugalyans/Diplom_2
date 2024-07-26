import pytest

from data import payload, REGISTER, AUTH
import requests

@pytest.fixture()
def make_new_user():
    response = requests.post(REGISTER, payload)
    token = response.json()['accessToken']
    yield response
    response = requests.delete(AUTH, headers={'Authorization': token})
