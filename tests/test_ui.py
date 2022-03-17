import allure
from objects import Base_page
from objects import Admin_page
import pytest
from objects import Registration_page
from objects import valute
from objects import input_product
from objects import product_add_func


@allure.feature("Тесты главной страницы.")
@allure.title("Переключение валют.")
@pytest.mark.parametrize("valute", valute)
def test_valute_button(browser, url_call, valute):
    base_page = Base_page(browser)
    base_page.open_base_page(url_call)
    base_page.valute_button(valute)


@allure.feature("Страница админки.")
@allure.title("Создание нового продукта в админке.")
def test_create_new_product(browser, url_call):
    """Тест создания нового продукта."""
    admin = Admin_page(browser)
    admin.open_admin_page(url_call)
    admin.admin_autorization()
    admin.product()
    admin.open_form_create_new_product()
    admin.input_product_name()
    admin.input_description_create_product()
    admin.input_metatag_create_product()
    admin.open_data_add_product()
    admin.input_model_data_addprod()
    admin.save_product_button()


@allure.feature("Тесты формы регистрации пользователя.")
@allure.title("Тест регистрация нового пользователя.")
def test_registration_new_user(browser, url_call):
    """Тест регистрации нового пользователя."""
    registration = Registration_page(browser)
    registration.open_registration_page(url_call)
    registration.input_first_name()
    registration.input_last_name()
    registration.input_email()
    registration.input_phone_number()
    registration.input_password()
    registration.input_password_confirm()
    registration.newsletter_no()
    registration.agree_privacy_policy()
    registration.continue_button()


@allure.feature("Тесты главной страницы.")
@allure.title("Тест открытия страницы Логин.")
def test_register_form_login(browser, url_call):
    """Тест проверяет работу раскрытия списка с регистрацией и авторизацией, открытие страницы Логина.
    Ожидаемый результат: Открытие страницы Логина."""
    registration = Base_page(browser)
    registration.open_base_page(url_call)
    registration.click_my_account()
    registration.click_my_account_login()
    registration.check_form_input_email_login()
    registration.check_form_input_password_login()
    registration.click_my_account_login_button()


@allure.feature("Тесты главной страницы.")
@allure.title("Проверка работоспособности поиска.")
@pytest.mark.parametrize("input_product", input_product)
def test_search_form(browser, url_call, input_product):
    """Тест проверяет работоспособность формы поиска."""
    registration = Base_page(browser)
    registration.open_base_page(url_call)
    registration.input_search_in_base_page(input_product)
    registration.click_button_search()
    registration.check_result_search()


@allure.feature("Тесты главной страницы.")
@allure.title("Появление аллерта при добавлении товара в корзину.")
@pytest.mark.parametrize("num", product_add_func())
def test_add_product_in_view_cart(browser, url_call, num):
    """Проверяем появление аллерта при добавлении товара в корзину."""
    addProduct = Base_page(browser)
    addProduct.open_base_page(url_call)
    addProduct.click_button_cart()
    addProduct.check_empty_cart()
    addProduct.click_add_product(num[1])
    addProduct.click_button_cart()
    addProduct.check_not_empty_cart()
