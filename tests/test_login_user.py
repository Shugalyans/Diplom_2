from data import payload, payload_for_login
from endpoints.users import User
import pytest
import allure


class TestLoginUser:

    @allure.title('Проверка: авторизация под существующим пользователем')
    @allure.description(
        'Проверяем, что можно авторизоваться под существующим пользователем'
    )
    def test_login_with_existing_user(self, make_new_user):
        new_user = User()
        response = new_user.login_user(payload)

        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Проверка: с пустыми\кривыми полями данных нельзя авторизоваться')
    @allure.description(
        'Проверяем, что нельзя авторизоваться, если поле логин или пароль неверные или пустые'
    )
    @pytest.mark.parametrize('new_data', payload_for_login)
    def test_create_user_but_mandatory_field_is_empty(self, make_new_user, new_data):
        new_user = User()
        response = new_user.login_user(new_data)

        assert response.status_code == 401 and "email or password are incorrect" in response.text
