class Order:
    data_for_order = {
        "firstName": "Stepan",
        "lastName": "Yakovlev",
        "address": "Some address",
        "metroStation": 10,
        "phone": "+7 915 275 33 94",
        "rentTime": 6,
        "deliveryDate": "2024-04-30",
        "comment": "Say something",
        "color": []
    }


class Url:
    create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    authorization_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    making_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'

class Msg:
    LOGIN_IS_BUSY = 'Этот логин уже используется. Попробуйте другой.'
    AUTH_BAD_REQUEST = 'Недостаточно данных для создания учетной записи'
    BAD_REQUEST = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'

