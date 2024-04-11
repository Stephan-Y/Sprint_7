import allure
import requests
from data import Url


class TestOrderList:

    @allure.title('Проверяем статусы успешных заказов и список заказов')
    def test_check_status_order_list(self):
        response = requests.get(Url.making_order)
        assert response.status_code == 200 and 'orders' in response.text
