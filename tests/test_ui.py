import allure
from objects import Base_page
from objects import Catalog_page
from objects import Product_card_page
from objects import Admin_page
import pytest
from objects import Registration_page

@allure.feature("Тесты главной страницы.")
@allure.title("Тест раскрытия списка регистрации и авторизации.")
def test_register_form(browser, url_call):
    """Тест проверяет работу раскрытия списка с регистрацией и авторизацией.
    Ожидаемый результат: Наличие в выпадающем списке Регистрации и Логина."""
    registration = Base_page(browser)
    registration.open_base_page(url_call)
    registration.click_my_account()