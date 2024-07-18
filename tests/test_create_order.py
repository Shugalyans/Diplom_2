from data import payload, ingredient, invalid_ingredient
from endpoints.orders import Order
from endpoints.users import User

import allure

class TestCreateOrder:

    @allure.title('Проверка: неавторизованный пользователь может сделать заказ')
    @allure.description(
        'Проверяем, что при неавторизированном пользователе можно сделать заказ. '
        'в документации API указано, что только авторизованные пользователи могут делать заказ. По факту работает не так, поэтому assertom проверяем код 200.'
    )
    def test_create_order_without_authorization(self):
        new_order = Order()
        response = new_order.create_new_order(ingredient)

#в документации API указано, что только авторизованные пользователи могут делать заказ. По факту работает не так, поэтому assertom проверяем код 200.
        assert response.status_code == 200 and 'number' in response.text

    @allure.title('Проверка: авторизованный пользователь может сделать заказ')
    @allure.description(
            'Проверяем, что авторизированному пользователю можно сделать заказ'
    )
    def test_create_order_with_authorization(self, make_new_user):
        make_new_user
        new_order = Order()
        new_user = User()
        new_user.login_user(payload)
        response = new_order.create_new_order(ingredient)

        assert response.status_code == 200 and 'number' in response.text


    @allure.title('Проверка: нельзя создать заказ без ингредиентов')
    @allure.description(
            'Проверяем, что нельзя сделать заказ без выбранных ингредиентов'
    )
    def test_create_order_without_ingredients(self, make_new_user):
        make_new_user
        new_order = Order()
        new_user = User()
        new_user.login_user(payload)
        response = new_order.create_new_order(None)

        assert response.status_code == 400 and 'Ingredient ids must be provided' in response.text

    @allure.title('Проверка: нельзя создать заказ с неверным хешем ингредиента')
    @allure.description(
            'Проверяем, что нельзя сделать заказ с неверным хешем ингредиента'
    )
    def test_create_order_with_wrong_ingredient_ID(self, make_new_user):
        make_new_user
        new_order = Order()
        new_user = User()
        new_user.login_user(payload)
        response = new_order.create_new_order(invalid_ingredient)

        assert response.status_code == 500 and 'Internal Server Error' in response.text
