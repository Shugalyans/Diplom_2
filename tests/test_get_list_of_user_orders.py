from data import payload, ingredient
from endpoints.orders import Order
from endpoints.users import User

import allure

class TestGetOrderList:

    @allure.title('Проверка: неавторизованному пользователю нельзя получить список заказов')
    @allure.description(
        'Проверяем, что при неавторизированном пользователе нельзя получить список заказов'
    )
    def test_get_order_list_without_authorization(self):
        new_order = Order()
        new_order.create_new_order(ingredient)

        orders_list = new_order.get_order_list(token=None)

        assert orders_list.status_code == 401 and 'You should be authorised' in orders_list.text

    @allure.title('Проверка: авторизованному пользователю можно получить список заказов')
    @allure.description(
        'Проверяем, что при авторизированном пользователе можно получить список его заказов'
    )
    def test_get_order_list_with_authorization(self, make_new_user):
        new_order = Order()
        new_user = User()
        token = new_user.get_token(payload)
        new_order.create_new_order(ingredient)

        orders_list = new_order.get_order_list(token)

        assert orders_list.status_code == 200 and 'totalToday' in orders_list.text