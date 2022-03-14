import pytest
import requests
import json
import allure

valute = ['USD', 'GBP', 'EUR']
session = requests.Session()
key = 'X0IzfMCLlfJ73jw21PM1aAwiO7vedjjzo7hoUl4EZPqfLNOX4f0lCcYvrosA3dwjBSiF3p1mfJGludwtB56P8eJx'


@pytest.fixture
def api_token(url_call):
    call = session.post(f'{url_call}index.php?route=api/login',
                        data={'username': 'user_tests', 'key': key})
    call_result = dict(json.loads(call.text))
    api_token = call_result['api_token']
    return api_token


@allure.feature("Тесты API.")
@allure.title("Метод авторизации.")
def test_api_login(url_call):
    call = session.post(f'{url_call}index.php?route=api/login',
                        data={'username': 'user_tests', 'key': key})
    assert dict(json.loads(call.text))['success'] == 'Success: API session successfully started!'


@allure.feature("Тесты API.")
@allure.title("Проверка валидности токена.")
def test_api_shipping_address(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/shipping/address',
                        params={'api_token': api_token}, data={'username': 'user_tests', 'key': key})
    assert call.status_code == 200 and call.headers is not None


@allure.feature("Тесты API.")
@allure.title("Метод смены валют.")
@pytest.mark.parametrize("valute", valute)
def test_api_currency(api_token, url_call, valute):
    call = session.post(f'{url_call}index.php?route=api/currency',
                        params={'api_token': api_token}, data={'currency': valute})
    assert dict(json.loads(call.text))['success'] == 'Success: Your currency has been changed!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод смены валют - некорректная валюта.")
def test_api_incorrect_currency(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/currency',
                        params={'api_token': api_token}, data={'currency': 'RUR'})
    assert dict(json.loads(call.text))['error'] == "Warning: Currency code is invalid!"
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод добавления товара в корзину.")
def test_api_cart_add(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/cart/add',
                        params={'api_token': api_token}, data={'product_id': '43', 'quantuty': '1'})
    assert dict(json.loads(call.text))['success'] == "Success: You have modified your shopping cart!"
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод добавления товара в корзину с несуществующим id.")
def test_api_cart_add_non_existent(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/cart/add',
                        params={'api_token': api_token}, data={'product_id': '1', 'quantuty': '1'})
    error = dict(json.loads(call.text))['error']
    assert error == {'store': 'Product can not be bought from the store you have choosen!'}
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод добавления товара в корзину с отрицательным числом товара.")
@pytest.mark.xfail(reason='Баг, принимает отрицательное число товара.')
def test_api_cart_add_negative_quantuty(api_token, url_call):
    """Тут есть баг, принимает отрицательное число товара."""
    call = session.post(f'{url_call}index.php?route=api/cart/add',
                        params={'api_token': api_token}, data={'product_id': '43', 'quantuty': '-10'})
    assert dict(json.loads(call.text)) == 'You cannot add a negative product number'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод изменения числа товара в корзине.")
def test_api_add_cart_edit(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/cart/edit',
                        params={'api_token': api_token}, data={'key': '43', 'quantuty': '1'})
    assert 'Success: You have modified your shopping cart!' in call.text
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод удаления товара в корзине.")
def test_api_add_cart_edit(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/cart/remove',
                        params={'api_token': api_token}, data={'key': '43'})
    assert dict(json.loads(call.text))['success'] == 'Success: You have modified your shopping cart!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод получения содержимого корзины.")
def test_api_add_cart_products(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/cart/products',
                        params={'api_token': api_token}, data={})
    result = dict(json.loads(call.text))
    assert (list(result.keys())) == ['products', 'vouchers', 'totals']
    assert (result['totals'][0]['title']) == 'Sub-Total'
    assert (result['totals'][1]['title']) == 'Total'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод применения купона.")
@pytest.mark.xfail(reason='Баг, не принимает валидные купоны.')
def test_api_coupons_valid(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/coupon',
                        params={'api_token': '19e49aacf28ece3e6d48a033b3'}, data={'coupon': '5555'})
    assert dict(json.loads(call.text))['success'] == 'Success: Coupon active!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод установить клиента для текущей сессии.")
def test_api_customers_valid(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/customer',
                        params={'api_token': api_token}, data={'firstname': 'User',
                                                               'lastname': 'Test1',
                                                               'email': 'test@mail.ru',
                                                               'telephone': '79998887766'})
    result = dict(json.loads(call.text))
    assert result["success"] == 'You have successfully modified customers'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод невалидного клиента для текущей сессии.")
def test_api_customers_invalid(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/customer',
                        params={'api_token': api_token}, data={})
    result = dict(json.loads(call.text))
    assert result["error"] == {'firstname': 'First Name must be between 1 and 32 characters!',
                               'lastname': 'Last Name must be between 1 and 32 characters!',
                               'email': 'E-Mail Address does not appear to be valid!',
                               'telephone': 'Telephone must be between 3 and 32 characters!'}
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Применить существующий сертификат.")
def test_api_voucher_valid(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/voucher',
                        params={'api_token': api_token}, data={'voucher': '1234'})
    result = dict(json.loads(call.text))
    assert result["success"] == 'Success: Your gift voucher discount has been applied!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Применить несуществующий сертификат.")
def test_api_voucher_invalid(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/voucher',
                        params={'api_token': api_token}, data={'voucher': 'Qwerty'})
    result = dict(json.loads(call.text))
    assert result["error"] == 'Warning: Gift Voucher is either invalid or the balance has been used up!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Добавить новый ваучер для текущей сессии.")
def test_api_voucher_add(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/voucher/add',
                        params={'api_token': api_token}, data={'from_name': 'User Test',
                                                               'from_email': 'admin@example.com',
                                                               'to_name': 'User Test',
                                                               'to_email': 'customer@example.com',
                                                               'amount': '100',
                                                               'code': 'VOU-7177'})
    result = dict(json.loads(call.text))
    assert result["success"] == 'Success: You have modified your shopping cart!'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Добавить невалидный ваучер для текущей сессии.")
def test_api_invalid_voucher_add(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/voucher/add',
                        params={'api_token': api_token}, data={})
    result = dict(json.loads(call.text))
    assert result["error"] == {'amount': 'Amount must be between $1.00 and $1,000.00!',
                               'from_email': 'E-Mail Address does not appear to be valid!',
                               'from_name': 'Your Name must be between 1 and 64 characters!',
                               'to_email': 'E-Mail Address does not appear to be valid!',
                               'to_name': "Recipient's Name must be between 1 and 64 characters!"}
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Установить адрес доставки для текущего сеанса.")
def test_api_shipping_address(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/shipping/address',
                        params={'api_token': api_token}, data={'firstname': 'Customer',
                                                               'lastname': 'Dear',
                                                               'address_1': 'Somewhere',
                                                               'city': 'KLD',
                                                               'country_id': 'RUS',
                                                               'zone_id': 'KGD'
                                                               })
    assert call.text == '[]'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Получаем доступные методы доставки.")
def test_api_shipping_methods(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/shipping/methods',
                        params={'api_token': api_token})
    assert dict(json.loads(call.text))["shipping_methods"] == []
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Получаем доступные методы доставки.")
def test_api_shipping_methods(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/shipping/methods',
                        params={'api_token': api_token})
    assert dict(json.loads(call.text))["shipping_methods"] == []
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Меняем доступные методы доставки.")
def test_api_shipping_method(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/shipping/method',
                        params={'api_token': api_token}, data={'shipping_method': 'pickup.pickup'})
    assert call.text == '[]'
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Метод Награда максимум.")
def test_api_reward_maximum(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/reward/maximum',
                        params={'api_token': api_token}, data={})
    assert dict(json.loads(call.text))['maximum'] == 0
    assert call.status_code == 200


@allure.feature("Тесты API.")
@allure.title("Установить адрес оплаты для этого сеанса.")
def test_api_payment_address(api_token, url_call):
    call = session.post(f'{url_call}index.php?route=api/payment/address',
                        params={'api_token': api_token}, data={'firstname': 'Customer',
                                                               'lastname': 'Dear',
                                                               'address_1': 'Somewhere',
                                                               'city': 'KLD',
                                                               'country_id': 'RUS',
                                                               'zone_id': 'KGD'})
    assert dict(json.loads(call.text))['success'] == "Success: Payment address has been set!"
    assert call.status_code == 200
