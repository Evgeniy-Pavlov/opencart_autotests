from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
import time
import logging
import allure
from selenium.common.exceptions import NoSuchElementException

valute = ("Euro", "Pound", "Dollar")
input_product = ("Mac", "hp", "lada")


def product_add_func():
    catalog = [("https://demo.opencart.com/index.php?route=product/product&product_id=43", "1"),
               ("https://demo.opencart.com/index.php?route=product/product&product_id=40", "2"),
               ]
    return catalog


class Base_page:
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)
        self.MY_ACCOUNT = (By.XPATH, "//*[@id=\"top-links\"]/ul/li[2]/a")
        self.MY_ACCOUNT_LOGIN = (By.XPATH, "//*[@id=\"top-links\"]/ul/li[2]/ul/li[2]/a")
        self.RETURNING_CUSTOMER = (By.XPATH, "//*[@id=\"content\"]/div/div[2]/div")
        self.RETURNING_CUSTOMER_FORM = (By.CSS_SELECTOR, ".well")
        self.RETURNING_CUSTOMER_INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
        self.RETURNING_CUSTOMER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
        self.RETURNING_CUSTOMER_LOGIN_BTN = (By.XPATH, "//*[@id=\"content\"]/div/div[2]/div/form/input")
        self.ADD_WISHLIST = (By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[3]/button[2]")
        self.ADD_PRODUCT = (By.XPATH, "//*[@id=\"content\"]/div[2]/div[]/div/div[3]/button[1]")
        self.BUTTON_CART = (By.CSS_SELECTOR, "#cart")
        self.CHECK_EMPTY_CART = (By.CSS_SELECTOR, ".text-center")
        self.CHECK_NOT_EMPTY_CART = (By.CSS_SELECTOR, ".table-striped")
        self.ADD_COMPRATION = (By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[3]/button[3]")
        self.VALUTE_MENU = (By.XPATH, "//*[@id=\"form-currency\"]/div/button")
        self.VALUTE_EURO = (By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[1]/button")
        self.VALUTE_POUND = (By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[2]/button")
        self.VALUTE_DOLLAR_US = (By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[3]/button")
        self.SEARCH_FORM = (By.CSS_SELECTOR, ".form-control")
        self.SEARCH_BUTTON = (By.CSS_SELECTOR, ".input-group-btn")
        self.SEARCH_RESULT_PRODUCT_DIV = (By.CSS_SELECTOR, ".product-layout")

    @allure.step("Открываем главную страницу.")
    def open_base_page(self, url=None):
        self.logger.info("Open url: {}".format(url))
        self.browser.get(url)

    @allure.step("Кликаем на иконку мой аккаунт.")
    def click_my_account(self):
        self.logger.info("Clicking element {}".format(self.MY_ACCOUNT))
        self.browser.find_element(*self.MY_ACCOUNT).click()

    @allure.step("Открываем страницу логина.")
    def click_my_account_login(self):
        self.logger.info("Clicking element {}".format("login"))
        WebDriverWait(self.browser, 2).until(es.presence_of_element_located(self.MY_ACCOUNT_LOGIN))
        self.browser.find_element(*self.MY_ACCOUNT_LOGIN).click()

    @allure.step("Проверяем наличие блока с полями для ввода логина(почты) и пароля.")
    def check_form_returning_customer(self):
        self.logger.info("Check form Returning Customer {}".format(self.RETURNING_CUSTOMER))
        WebDriverWait(self.browser, 2).until(es.presence_of_element_located(self.RETURNING_CUSTOMER))
        self.browser.find_element(*self.RETURNING_CUSTOMER_FORM)

    @allure.step("Проверяем наличие и ввод поля E-Mail Address.")
    def check_form_input_email_login(self):
        self.logger.info("Check #input-email")
        self.browser.find_element(*self.RETURNING_CUSTOMER_INPUT_EMAIL).clear()
        self.logger.info("Input #input-email")
        self.browser.find_element(*self.RETURNING_CUSTOMER_INPUT_EMAIL).send_keys("test@mail.ru")

    @allure.step("Проверяем наличие поля для ввода пароля.")
    def check_form_input_password_login(self):
        self.logger.info("Check #input-password")
        self.browser.find_element(*self.RETURNING_CUSTOMER_INPUT_PASSWORD).clear()
        self.logger.info("Input #input-password")
        self.browser.find_element(*self.RETURNING_CUSTOMER_INPUT_PASSWORD).send_keys("1234")

    @allure.step("Нажимаем на кнопку login в форме авторизации.")
    def click_my_account_login_button(self):
        self.logger.info("Clicking element-button {}".format("btn btn-primary"))
        self.browser.find_element(*self.RETURNING_CUSTOMER_LOGIN_BTN).click()

    @allure.step("Добавляем товар в вишлист.")
    def click_add_wishlist(self):
        self.logger.info("Clicking element: wishlist")
        self.browser.find_element(*self.ADD_WISHLIST).click()

    @allure.step("Добавляем товар в корзину.")
    def click_add_product(self, num=str()):
        self.logger.info("Clicking element: button 'add product'")
        self.browser.find_element(
            By.XPATH, "//*[@id=\"content\"]/div[2]/div[{}]/div/div[3]/button[1]".format(num)).click()

    @allure.step("Открываем список добавленных в корзину товаров.")
    def click_button_cart(self):
        self.logger.info("Clicking element: #cart")
        self.browser.find_element(*self.BUTTON_CART).click()

    @allure.step("Проверяем, что корзина пустая.")
    def check_empty_cart(self):
        self.logger.info("Check element: .text-center")
        self.browser.find_element(*self.CHECK_EMPTY_CART)

    @allure.step("Проверяем, что корзина не пустая. В корзине добавлен товар.")
    def check_not_empty_cart(self):
        self.logger.info("Check element: .table-striped")
        self.browser.find_element(*self.CHECK_NOT_EMPTY_CART)

    @allure.step("Добавляем товар к сравнению.")
    def click_add_comparison(self, num=str()):
        self.logger.info("Clicking element: button 'add comparison'")
        self.browser.find_element(
            By.XPATH, "//*[@id=\"content\"]/div[2]/div[{}]/div/div[3]/button[3]".format(num)).click()

    @allure.step("Переключаем валюту.")
    def valute_button(self, valute):
        self.logger.info("Click valute menu.")
        self.browser.find_element(*self.VALUTE_MENU).click()
        if valute == "Euro":
            self.browser.find_element(*self.VALUTE_EURO).click()
        elif valute == "Pound":
            self.browser.find_element(*self.VALUTE_POUND).click()
        elif valute == "Dollar":
            self.browser.find_element(*self.VALUTE_DOLLAR_US).click()

    @allure.step("Вводим в поле поиск.")
    def input_search_in_base_page(self, input_product):
        self.logger.info("Clicking element: .form-control")
        self.browser.find_element(*self.SEARCH_FORM).clear()
        self.logger.info("Input in .form-control")
        self.browser.find_element(*self.SEARCH_FORM).send_keys(input_product)

    @allure.step("Нажимаем на кнопку поиска.")
    def click_button_search(self):
        self.logger.info("Clicking element: .input-group-btn")
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    @allure.step("Проверяем наличие результатов поиска.")
    def check_result_search(self):
        try:
            self.logger.info("Search element: .product-layout")
            self.browser.find_element(*self.SEARCH_RESULT_PRODUCT_DIV)
        except NoSuchElementException as nee:
            raise AssertionError(nee)


class Catalog_page(Base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.CATALOG_LEFT_PANEL_LAPTOP = (By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[2]")
        self.CATALOG_LEFT_PANEL_COMPONENTS = (By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[3]")
        self.CATALOG_LEFT_PANEL_PHONES = (By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[6]")
        self.CATALOG_GRID_VIEW = (By.CSS_SELECTOR, "#grid-view")
        self.CATALOG_LIST_VIEW = (By.CSS_SELECTOR, "#list-view")
        self.CATALOG_SORT_BY_BTN = (By.XPATH, "//*[@id=\"input-sort\"]")

    @allure.step("Открываем раздел Каталог- ПК.")
    def open_desktop_catalog(self, url):
        self.logger.info("Open url: {}".format(url))
        self.browser.get(url + "index.php?route=product/category&path=18")

    @allure.step("Добавляем товар в вишлист.")
    def click_left_panel_laptop(self):
        self.logger.info("Open left panel.")
        self.browser.find_element(*self.CATALOG_LEFT_PANEL_LAPTOP).click()

    @allure.step("Кликаем на левую панель компоненты.")
    def click_left_panel_components(self):
        self.logger.info("Clicking left panel components.")
        self.browser.find_element(*self.CATALOG_LEFT_PANEL_COMPONENTS).click()

    @allure.step("Кликаем на левой панели телефоны.")
    def click_left_panel_phones(self):
        self.logger.info("Clicking panel phones.")
        self.browser.find_element(*self.CATALOG_LEFT_PANEL_PHONES).click()

    @allure.step("Кликаем на меню грид.")
    def click_grid_view(self):
        self.logger.info("Clicking grid menu.")
        self.browser.find_element(*self.CATALOG_GRID_VIEW).click()

    @allure.step("Кликаем на меню лист.")
    def click_list_view(self):
        self.logger.info("Clicking list menu.")
        self.browser.find_element(*self.CATALOG_LIST_VIEW).click()

    @allure.step("Кликаем на кнопку сортировки.")
    def click_sort_by(self):
        self.logger.info("Clicking button sort by.")
        self.browser.find_element(*self.CATALOG_SORT_BY_BTN).click()


class Product_card_page(Base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.FORM_REVIEW = (By.XPATH, "//*[@id=\"content\"]/div[1]/div[1]/ul[2]/li[2]/a")
        self.PRODUCT_DESCRIPTION = (By.XPATH, "//*[@id=\"content\"]/div[1]/div[1]/ul[2]/li[1]/a")
        self.INPUT_QUANTITY = (By.CSS_SELECTOR, "#input-quantity")
        self.PRODUCT_BUTTON_TO_CART = (By.CSS_SELECTOR, "#button-cart")
        self.PRODUCT_DROPDOWN_MENU = (By.CSS_SELECTOR, "#cart")

    @allure.step("Открываем страницу продукта.")
    def open_desktop_card(self, url):
        self.logger.info("Open url: {}".format(url))
        self.browser.get(url + "index.php?route=product/product&path=20_27&product_id=41")

    @allure.step("Открываем форму ревью.")
    def click_form_review(self):
        self.logger.info("Clicking form review")
        self.browser.find_element(*self.FORM_REVIEW).click()

    @allure.step("Открываем форму описание.")
    def click_desriprion(self):
        self.logger.info("Click description.")
        self.browser.find_element(*self.PRODUCT_DESCRIPTION).click()

    @allure.step("Изменяем число товара.")
    def edit_qty(self):
        self.logger.info("Click #input-quantity")
        self.browser.find_element(*self.INPUT_QUANTITY).clear()
        self.logger.info("Click #input-quantity")
        self.browser.find_element(*self.INPUT_QUANTITY).send_keys("2")

    @allure.step("Добавляем ПК в корзину.")
    def add_to_cart_pc(self):
        self.logger.info("Click 'add to cart'")
        self.browser.find_element(*self.PRODUCT_BUTTON_TO_CART).click()

    @allure.step("Открываем выпадающее меню.")
    def dropdown_menu(self):
        self.logger.info("Click dropdown menu.")
        self.browser.find_element(*self.PRODUCT_DROPDOWN_MENU).click()


class Admin_page(Base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.ADMIN_AUTHORIZATION_INPUT_USER = (By.CSS_SELECTOR, "#input-username")
        self.ADMIN_AUTHORIZATION_INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
        self.ADMIN_AUTHORIZATION_LOGIN_BTN = (
            By.XPATH, "//*[@id=\"content\"]/div/div/div/div/div[2]/form/div[3]/button")
        self.ADMIN_CATALOG = (By.XPATH, "//*[@id=\"menu-catalog\"]")
        self.ADMIN_CATALOG_CATEGORIES = (By.XPATH, "//*[@id=\"collapse1\"]/li[1]/a")
        self.ADMIN_CATALOG_PRODUCTS = (By.XPATH, "//*[@id=\"collapse1\"]/li[2]")
        self.ADMIN_PRODUCTS_ADD_NEW_BTN = (By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a")
        self.ADMIN_PRODUCTS_DELETE_PROD_BTN = (By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button[3]")
        self.ADMIN_PRODUCT_CHECKBOX_PROD_DEL = (By.XPATH, "//*[@id=\"form-product\"]/div/table/tbody/tr[1]/td[1]/input")
        self.ADMIN_PRODUCT_INPUT_PROD_NAME = (By.CSS_SELECTOR, "#input-name1")
        self.ADMIN_PRODUCT_CREATE_INPUT_DESCRIPTION = (By.XPATH, "//*[@id=\"language1\"]/div[2]/div/div/div[3]/div[2]")
        self.ADMIN_PRODUCT_CREATE_INPUT_METATAG = (By.CSS_SELECTOR, "#input-meta-title1")
        self.ADMIN_PRODUCT_CREATE_INPUT_OPENDATA = (By.XPATH, "//*[@id=\"form-product\"]/ul/li[2]/a")
        self.ADMIN_PRODUCT_CREATE_INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
        self.ADMIN_PRODUCT_CREATE_SAVE = (By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button")
        self.ADMIN_SETTING_BTN = (By.CSS_SELECTOR, "#button-setting")
        self.ADMIN_PEOPLE_ONLINE = (By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div[4]/div/div[3]/a")
        self.ADMIN_CREATE_NEW_CATEGORY = (By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a[1]")

    @allure.step("Открываем старницу админки.")
    def open_admin_page(self, url):
        self.logger.info("Open url: {}".format(url))
        self.browser.get(url + "admin/")

    @allure.step("Проходим авторизацию авторизацию.")
    def admin_autorization(self):
        self.logger.info("Clear #input-username.")
        self.browser.find_element(*self.ADMIN_AUTHORIZATION_INPUT_USER).clear()
        self.logger.info("Clear #input-password.")
        self.browser.find_element(*self.ADMIN_AUTHORIZATION_INPUT_PASSWORD).clear()
        self.logger.info("Input #input-username.")
        self.browser.find_element(*self.ADMIN_AUTHORIZATION_INPUT_USER).send_keys("user")
        self.logger.info("Input #input-password.")
        self.browser.find_element(*self.ADMIN_AUTHORIZATION_INPUT_PASSWORD).send_keys("bitnami")
        self.logger.info("Click button Login.")
        self.browser.find_element(*self.ADMIN_AUTHORIZATION_LOGIN_BTN).click()

    @allure.step("Кликаем на кнопку сортировки.")
    def categories(self):
        self.logger.info("Open menu-catalog.")
        self.browser.find_element(*self.ADMIN_CATALOG).click()
        time.sleep(2)
        self.logger.info("Click menu categories.")
        self.browser.find_element(*self.ADMIN_CATALOG_CATEGORIES).click()

    @allure.step("Открываем раздел продукты.")
    def product(self):
        self.logger.info("Click menu.")
        self.browser.find_element(*self.ADMIN_CATALOG).click()
        time.sleep(2)
        self.logger.info("Click products.")
        self.browser.find_element(*self.ADMIN_CATALOG_PRODUCTS).click()

    @allure.step("Открываем форму создания нового продукта.")
    def open_form_create_new_product(self):
        self.logger.info("Click create product.")
        self.browser.find_element(*self.ADMIN_PRODUCTS_ADD_NEW_BTN).click()

    @allure.step("Открываем форму удаления продукта.")
    def open_form_delete_product(self):
        self.logger.info("Open form delete product.")
        self.browser.find_element(*self.ADMIN_PRODUCTS_DELETE_PROD_BTN).click()

    @allure.step("Кликаем на чекбокс удаления продукта.")
    def checkbox_product_delete(self):
        self.logger.info("Click menu categories.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CHECKBOX_PROD_DEL).click()

    @allure.step("Вводим имя продукта.")
    def input_product_name(self):
        self.logger.info("Clear #input-name1.")
        self.browser.find_element(*self.ADMIN_PRODUCT_INPUT_PROD_NAME).clear()
        self.logger.info("Input #input-name1.")
        self.browser.find_element(*self.ADMIN_PRODUCT_INPUT_PROD_NAME).send_keys("Test_product")

    @allure.step("Вводим описания нового продукта.")
    def input_description_create_product(self):
        self.logger.info("Clear description.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_DESCRIPTION).clear()
        self.logger.info("Input description.")
        self.browser.find_element(
            *self.ADMIN_PRODUCT_CREATE_INPUT_DESCRIPTION).send_keys("Description test product.")

    @allure.step("Вводим метатэг нового продукта.")
    def input_metatag_create_product(self):
        self.logger.info("Clear metatag.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_METATAG).clear()
        self.logger.info("Input metatag.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_METATAG).send_keys("Test_product")

    @allure.step("Вводим данные об новом продукте.")
    def open_data_add_product(self):
        self.logger.info("Clicking open data add product.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_OPENDATA).click()

    @allure.step("Вводим модель нового продукта.")
    def input_model_data_addprod(self):
        self.logger.info("Clear model product.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_MODEL).clear()
        self.logger.info("Input model product.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_INPUT_MODEL).send_keys("12T")

    @allure.step("Сохраняем новый продукт.")
    def save_product_button(self):
        self.logger.info("Clicking button save product.")
        self.browser.find_element(*self.ADMIN_PRODUCT_CREATE_SAVE).click()

    @allure.step("Кликаем на кнопку настроек.")
    def button_setting(self):
        self.logger.info("Click admin setting.")
        self.browser.find_element(*self.ADMIN_SETTING_BTN).click()

    @allure.step("Открываем меню пользователей в сети.")
    def people_online(self):
        self.logger.info("Open form people online.")
        self.browser.find_element(*self.ADMIN_PEOPLE_ONLINE).click()

    @allure.step("Открываем форму создания новой категории.")
    def create_new_category(self):
        self.logger.info("Open form create new category.")
        self.browser.find_element(*self.ADMIN_CREATE_NEW_CATEGORY).click()


class Registration_page(Base_page):
    def __init__(self, browser):
        super().__init__(browser)
        self.REG_INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
        self.REG_INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
        self.REG_INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
        self.REG_INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
        self.REG_INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
        self.REG_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
        self.REG_NEWSLETTERS_NO = (By.XPATH, "//*[@id=\"content\"]/form/fieldset[3]/div/div/label[2]/input")
        self.REG_NEWSLETTERS_YES = (By.XPATH, "//*[@id=\"content\"]/form/fieldset[3]/div/div/label[1]/input")
        self.AGREE_PRIVACY_POLICY = (By.XPATH, "//*[@id=\"content\"]/form/div/div/input[1]")
        self.REG_CONTINUE_BUTTON = (By.XPATH, "//*[@id=\"content\"]/form/div/div/input[2]")

    @allure.step("Открываем страницу регистрации.")
    def open_registration_page(self, url):
        self.logger.info("Open url: {}".format(url))
        self.browser.get(url + "/index.php?route=account/register")

    @allure.step("Вводим имя нового пользователя.")
    def input_first_name(self):
        self.logger.info("Clear form first name.")
        self.browser.find_element(*self.REG_INPUT_FIRSTNAME).clear()
        self.logger.info("Input first name.")
        self.browser.find_element(*self.REG_INPUT_FIRSTNAME).send_keys("Evgeniy")

    @allure.step("Вводим фамилию нового пользователя.")
    def input_last_name(self):
        self.logger.info("Clear form first name.")
        self.browser.find_element(*self.REG_INPUT_LASTNAME).clear()
        self.logger.info("Input last name.")
        self.browser.find_element(*self.REG_INPUT_LASTNAME).send_keys("Pavlov")

    @allure.step("Ввести почтовый ящик.")
    def input_email(self):
        self.logger.info("Clear form email.")
        self.browser.find_element(*self.REG_INPUT_EMAIL).clear()
        self.logger.info("Input email.")
        self.browser.find_element(*self.REG_INPUT_EMAIL).send_keys("test2@yandex.ru")

    @allure.step("Ввод номера телефона.")
    def input_phone_number(self):
        self.logger.info("Clear form phone.")
        self.browser.find_element(*self.REG_INPUT_TELEPHONE).clear()
        self.logger.info("Input phone.")
        self.browser.find_element(*self.REG_INPUT_TELEPHONE).send_keys("+79999989796")

    @allure.step("Ввод пароля.")
    def input_password(self):
        self.logger.info("Clear password.")
        self.browser.find_element(*self.REG_INPUT_PASSWORD).clear()
        self.logger.info("Input password.")
        self.browser.find_element(*self.REG_INPUT_PASSWORD).send_keys("user")

    @allure.step("Ввод подтверждения пароля.")
    def input_password_confirm(self):
        self.logger.info("Clear confirm password.")
        self.browser.find_element(*self.REG_INPUT_PASSWORD_CONFIRM).clear()
        self.logger.info("Input confirm password.")
        self.browser.find_element(*self.REG_INPUT_PASSWORD_CONFIRM).send_keys("user")

    @allure.step("Выключаем согласия на рассылку.")
    def newsletter_no(self):
        self.logger.info("Click newsletters no.")
        self.browser.find_element(*self.REG_NEWSLETTERS_NO).click()

    @allure.step("Включаем согласие на рассылку.")
    def newsletter_yes(self):
        self.logger.info("Click newsletters yes.")
        self.browser.find_element(*self.REG_NEWSLETTERS_YES).click()

    @allure.step("Соглашаемся с пользовательским соглашением.")
    def agree_privacy_policy(self):
        self.logger.info("Click agree policy.")
        self.browser.find_element(*self.AGREE_PRIVACY_POLICY).click()

    @allure.step("Нажимаем кнопку продолжить.")
    def continue_button(self):
        self.logger.info("Click button continue.")
        self.browser.find_element(*self.REG_CONTINUE_BUTTON).click()
