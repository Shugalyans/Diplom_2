import allure
import pytest

from data import payload, payload_for_empty_fields
from endpoints.users import User


class TestCreateUser:

    @allure.title('Проверка: создание нового пользователя')
    @allure.description(
        'Проверяем, что можно создать уникального пользователя'
    )
    def test_create_new_user(self, make_new_user):
        response = make_new_user

        assert response.status_code == 200 and "accessToken" in response.text

    @allure.title('Проверка: нельзя создать двух одинаковых пользователей')
    @allure.description(
        'Проверяем, что пользователя с одинаковыми данными нельзя создать дважды'
    )
    def test_create_the_same_user(self, make_new_user):
        new_user = User()

        response = new_user.create_new_user(payload)

        assert response.status_code == 403 and "User already exists" in response.text

    @allure.title('Проверка: для создания пользователя нужно заполнить все обязательные поля')
    @allure.description(
        'Проверяем, что можно для создания пользователя нужно заполнить все обязательные поля'
    )
    @pytest.mark.parametrize('new_data', payload_for_empty_fields)
    def test_create_user_but_mandatory_field_is_empty(self, new_data):
        new_user = User()

        response = new_user.create_new_user(new_data)

        assert response.status_code == 403 and "Email, password and name are required fields" in response.text