
URL = 'https://stellarburgers.nomoreparties.site/api/'

payload = {
        "email": "Shemakhanskiy@yandex.ru",
        "password": "12345678",
        "name": "Mikhail"
    }

payload_for_empty_fields = [
    {
        "email": None,
        "password": "12345678",
        "name": "Mikhail"
    },
    {
        "email": "Shemakhanskiy@yandex.ru",
        "password": None,
        "name": "Mikhail"
    },
    {
        "email": "Shemakhanskiy@yandex.ru",
        "password": "12345678",
        "name": None
    }
]

payload_for_login = [
    {
        "email": None,
        "password": "12345678",
        "name": "Mikhail"
    },
    {
        "email": "Shemakhanskiy@yandex.ru",
        "password": None,
        "name": "Mikhail"
    },
    {
        "email": "Shemakhanskiyy@yandex.ru",
        "password": "12345678",
        "name": "Mikhail"
    },
    {
        "email": "Shemakhanskiy@yandex.ru",
        "password": "123456789",
        "name": "Mikhail"
    }

]

edited_profile = [
   {
    "email": "Shemakhanskiy1@yandex.ru",
    "name": "Mikhail"
   },
   {
    "email": "Shemakhanskiy@yandex.ru",
    "name": "Mikhail1"
   }
]

ingredient = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa72"]}
invalid_ingredient = {"ingredients": ["61c0c5a71d1f82001bdaaa","61c0c5a71d1f82001bdaaa72"]}
