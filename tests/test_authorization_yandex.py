import pytest
from dotenv import dotenv_values
from authorization_yandex import entering_form

env_values = dotenv_values('api_key.env')
@pytest.mark.parametrize(
        "user_possible_input, expected",
        [
            [' ', 'Логин не указан'],
            ['51346773', 'Такой логин не подойдет'],
            ['&!@#$%^*()', 'Такой логин не подойдет'],
            [env_values.get("YANDEX_LOGIN"), 'Все указано верно'],
            ['wrong_password', 'Неверный пароль'],
            [' ', 'Пароль не указан'],
            [env_values.get("YANDEX_PASSWORD"), 'Все указано верно']
        ]
)
def test_authorization(user_possible_input, expected):
    result = entering_form(user_possible_input)
    assert expected == result