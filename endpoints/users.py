import requests
from data import URL

class User:

    def create_new_user(self, payload):
        response = requests.post(f'{URL}auth/register', payload)
        return response

    def login_user(self, payload):
        response = requests.post(f'{URL}auth/login', payload)
        return response

    def delete_user(self, token):
        self.response = requests.delete(f'{URL}auth/user', headers={'Authorization': token})

    def edit_user(self, edited_profile, token):
        response = requests.patch(f'{URL}auth/user', data=edited_profile, headers={'Authorization': token})
        return response

    def get_token(self, payload):
        response = requests.post(f'{URL}auth/login', payload)

        token = response.json()['accessToken']
        return token







