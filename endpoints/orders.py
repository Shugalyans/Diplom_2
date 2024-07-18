import requests
from data import URL

class Order:


    def create_new_order(self, ingredient):
        response = requests.post(f'{URL}orders', ingredient)
        return response

    def get_order_list(self, token):
        response = requests.get(f'{URL}orders', headers={'Authorization': token})
        return response