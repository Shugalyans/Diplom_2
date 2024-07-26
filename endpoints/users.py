import requests
from data import REGISTER, LOGIN, AUTH

class User:

    def create_new_user(self, payload):
        response = requests.post(REGISTER, payload)
        return response

    def login_user(self, payload):
        response = requests.post(LOGIN, payload)
        return response

    def delete_user(self, token):
        self.response = requests.delete(AUTH, headers={'Authorization': token})

    def edit_user(self, edited_profile, token):
        response = requests.patch(AUTH, data=edited_profile, headers={'Authorization': token})
        return response

    def get_token(self, payload):
        response = requests.post(LOGIN, payload)

        token = response.json()['accessToken']
        return token







