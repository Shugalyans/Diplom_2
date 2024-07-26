from data import payload, edited_profile
from endpoints.users import User
import pytest
import allure

class TestEditUser:

    @allure.title('Проверка: изменение данных авторизованного пользователя')
    @allure.description(
        'Проверяем, что можно изменить данные пользователя если авторизован под ним'
    )
    @pytest.mark.parametrize('profile_value', edited_profile)
    def test_edit_authorized_user(self, make_new_user, profile_value):
        new_user = User()
        token = new_user.get_token(payload)
        response = new_user.edit_user(profile_value, token)

        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Проверка: изменение данных неавторизованного пользователя')
    @allure.description(
        'Проверяем, что нельзя изменить данные пользователя если не авторизоваться под ним'
    )
    @pytest.mark.parametrize('profile_value', edited_profile)
    def test_edit_user_without_authorization(self, make_new_user, profile_value):
        new_user = User()
        response = new_user.edit_user(profile_value, token=None)

        assert response.status_code == 401 and "You should be authorised" in response.text
