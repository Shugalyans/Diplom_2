import requests
from data import ORDERS

class Order:


    def create_new_order(self, ingredient):
        response = requests.post(ORDERS, ingredient)
        return response

    def get_order_list(self, token):
        response = requests.get(ORDERS, headers={'Authorization': token})
        return response