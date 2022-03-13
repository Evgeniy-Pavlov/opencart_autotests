from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import logging
import allure


class Base_page():
    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Открываем главную страницу.")
    def open_base_page(self, url=None):
        try:
            self.logger.info("Open url: {}".format(url))
            self.browser.get(url)
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на иконку мой аккаунт.")
    def click_my_account(self):
        try:
            self.logger.info("Clicking element {}".format(".dropdown"))
            self.browser.find_element(By.CSS_SELECTOR, ".dropdown").click()

        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Добавляем товар в вишлист.")
    def click_add_wishlist(self):
        try:
            self.logger.info("Clicking element: wishlist")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[3]/button[2]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Добавляем товар в корзину.")
    def click_add_product(self, num=str()):
        try:
            self.logger.info("Clicking element: button 'add product'")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"content\"]/div[2]/div[" + num + "]/div/div[3]/button[1]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)


    @allure.step("Добавляем товар к сравнению.")
    def click_add_comparison(self, num=str()):
        try:
            self.logger.info("Clicking element: button 'add comparison'")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"content\"]/div[2]/div[" + num + "]/div/div[3]/button[3]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Переключаем валюту.")
    def valute_button(self, valute):
        try:
            self.logger.info("Click valute menu.")
            self.browser.find_element(By.XPATH, "//*[@id=\"form-currency\"]/div/button").click()
            if valute == "Euro":
                self.browser.find_element(
                    By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[1]/button").click()
            elif valute == "Pound":
                self.browser.find_element(
                    By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[2]/button").click()
            elif valute == "Dollar":
                self.browser.find_element(
                    By.XPATH, "//*[@id=\"form-currency\"]/div/ul/li[3]/button").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)


class Catalog_page(Base_page):
    @allure.step("Открываем раздел Каталог- ПК.")
    def open_desktop_catalog(self, url):
        try:
            self.logger.info("Open url: {}".format(url))
            self.browser.get(url + "index.php?route=product/category&path=18")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Добавляем товар в вишлист.")
    def click_left_panel_laptop(self):
        try:
            self.logger.info("Open left panel.")
            self.browser.find_element(By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[2]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на левую панель компоненты.")
    def click_left_panel_components(self):
        try:
            self.logger.info("Clicking left panel components.")
            self.browser.find_element(By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[3]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на левой панели телефоны.")
    def click_left_panel_phones(self):
        try:
            self.logger.info("Clicking panel phones.")
            self.browser.find_element(By.XPATH, "//*[@id=\"column-left\"]/div[1]/a[6]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на меню грид.")
    def click_grid_view(self):
        try:
            self.logger.info("Clicking grid menu.")
            self.browser.find_element(By.CSS_SELECTOR, "#grid-view").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на меню лист.")
    def click_list_view(self):
        try:
            self.logger.info("Clicking list menu.")
            self.browser.find_element(By.CSS_SELECTOR, "#list-view").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на кнопку сортировки.")
    def click_sort_by(self):
        try:
            self.logger.info("Clicking button sort by.")
            self.browser.find_element(By.XPATH, "//*[@id=\"input-sort\"]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)


class Product_card_page(Base_page):
    @allure.step("Открываем страницу продукта.")
    def open_desktop_card(self, url):
        try:
            self.logger.info("Open url: {}".format(url))
            self.browser.get(url + "index.php?route=product/product&path=20_27&product_id=41")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем форму ревью.")
    def click_form_review(self):
        try:
            self.logger.info("Clicking form review")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div[1]/ul[2]/li[2]/a")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем форму описание.")
    def click_desriprion(self):
        try:
            self.logger.info("Click description.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div[1]/ul[2]/li[1]/a")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Изменяем число товара.")
    def edit_qty(self):
        try:
            self.logger.info("Click #input-quantity")
            self.browser.find_element(By.CSS_SELECTOR, "#input-quantity").clear()
            self.logger.info("Click #input-quantity")
            self.browser.find_element(By.CSS_SELECTOR, "#input-quantity").send_keys("2")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Добавляем ПК в корзину.")
    def add_to_cart_pc(self):
        try:
            self.logger.info("Click 'add to cart'")
            self.browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем выпадающее меню.")
    def dropdown_menu(self):
        try:
            self.logger.info("Click dropdown menu.")
            self.browser.find_element(By.CSS_SELECTOR, "#cart").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)


class Admin_page(Base_page):
    @allure.step("Открываем старницу админки.")
    def open_admin_page(self, url):
        try:
            self.logger.info("Open url: {}".format(url))
            self.browser.get(url + "admin/")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Проходим авторизацию авторизацию.")
    def admin_autorization(self):
        try:
            self.logger.info("Clear #input-username.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-username").clear()
            self.logger.info("Clear #input-password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").clear()
            self.logger.info("Input #input-username.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("demo")
            self.logger.info("Clear #input-password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("demo")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"content\"]/div/div/div/div/div[2]/form/div[3]/button").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на кнопку сортировки.")
    def categories(self):
        try:
            self.logger.info("Open menu-catalog.")
            self.browser.find_element(By.CSS_SELECTOR, "#menu-catalog > a").click()
            time.sleep(2)
            self.logger.info("Click menu categories.")
            self.browser.find_element(By.XPATH, "//*[@id=\"collapse1\"]/li[1]/a").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем раздел продукты.")
    def product(self):
        try:
            self.logger.info("Click menu.")
            self.browser.find_element(By.XPATH, "//*[@id=\"menu-catalog\"]/a").click()
            time.sleep(2)
            self.logger.info("Click product.")
            self.browser.find_element(By.XPATH, "//*[@id=\"collapse1\"]/li[2]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем форму создания нового продукта.")
    def open_form_create_new_product(self):
        try:
            self.logger.info("Click create product.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем форму удаления продукта.")
    def open_form_delete_product(self):
        try:
            self.logger.info("Open form delete product.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button[3]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на чекбокс удаления продукта.")
    def checkbox_product_delete(self):
        try:
            self.logger.info("Click menu categories.")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"form-product\"]/div/table/tbody/tr[1]/td[1]/input").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим имя продукта.")
    def input_product_name(self):
        try:
            self.logger.info("Clear #input-name1.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-name1").clear()
            self.logger.info("Input #input-name1.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-name1").send_keys("Test_product")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим описания нового продукта.")
    def input_description_create_product(self):
        try:
            self.logger.info("Clear description.")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"language1\"]/div[2]/div/div/div[3]/div[2]").clear()
            self.logger.info("Input description.")
            self.browser.find_element(
                By.XPATH, "//*[@id=\"language1\"]/div[2]/div/div/div[3]/div[2]").send_keys("Description test product.")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим метатэг нового продукта.")
    def input_metatag_create_product(self):
        try:
            self.logger.info("Clear metatag.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title1").clear()
            self.logger.info("Input metatag.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-meta-title1").send_keys("Test_product")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим данные об новом продукта.")
    def open_data_add_product(self):
        try:
            self.logger.info("Clicking open data add product.")
            self.browser.find_element(By.XPATH, "//*[@id=\"form-product\"]/ul/li[2]/a").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим модель нового продукта.")
    def input_model_data_addprod(self):
        try:
            self.logger.info("Clear model product.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-model").clear()
            self.logger.info("Input model product.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-model").send_keys("12T")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Сохраняем новый продукт.")
    def save_product_button(self):
        try:
            self.logger.info("Clicking button save product.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/button").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Кликаем на кнопку настроек.")
    def button_setting(self):
        try:
            self.logger.info("Click admin setting.")
            self.browser.find_element(By.CSS_SELECTOR, "#button-setting").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем меню пользователей в сети.")
    def people_online(self):
        try:
            self.logger.info("Open form people online.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div[4]/div/div[3]/a").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Открываем форму создания новой категории.")
    def create_new_category(self):
        try:
            self.logger.info("Open form create new category.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/a[1]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)


class Registration_page(Base_page):
    @allure.step("Открываем страницу регистрации.")
    def open_registration_page(self, url):
        try:
            self.logger.info("Open url: {}".format(url))
            self.browser.get(url + "/index.php?route=account/register")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим имя нового пользователя.")
    def input_first_name(self):
        try:
            self.logger.info("Clear form first name.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-firstname").clear()
            self.logger.info("Input first name.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-firstname").send_keys("Evgeniy")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Вводим фамилию нового пользователя.")
    def input_last_name(self):
        try:
            self.logger.info("Clear form first name.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-lastname").clear()
            self.logger.info("Input last name.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-lastname").send_keys("Pavlov")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Ввести почтовый ящик.")
    def input_email(self):
        try:
            self.logger.info("Clear form email.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-email").clear()
            self.logger.info("Input email.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("test2@yandex.ru")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Ввод номера телефона.")
    def input_phone_number(self):
        try:
            self.logger.info("Clear form phone.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-telephone").clear()
            self.logger.info("Input phone.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-telephone").send_keys("+79999989796")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Ввод пароля.")
    def input_password(self):
        try:
            self.logger.info("Clear password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").clear()
            self.logger.info("Input password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("user")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Ввод подтверждения пароля.")
    def input_password_confirm(self):
        try:
            self.logger.info("Clear confirm password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-confirm").clear()
            self.logger.info("Input confirm password.")
            self.browser.find_element(By.CSS_SELECTOR, "#input-confirm").send_keys("user")
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Выключаем согласия на рассылку.")
    def newsletter_no(self):
        try:
            self.logger.info("Click newsletters no.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/form/fieldset[3]/div/div/label[2]/input").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Включаем согласие на рассылку.")
    def newsletter_yes(self):
        try:
            self.logger.info("Click newsletters yes.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/form/fieldset[3]/div/div/label[1]/input").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Соглашаемся с пользовательским соглашением.")
    def agree_privacy_policy(self):
        try:
            self.logger.info("Click agree policy.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/form/div/div/input[1]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)

    @allure.step("Нажимаем кнопку продолжить.")
    def continue_button(self):
        try:
            self.logger.info("Click button continue.")
            self.browser.find_element(By.XPATH, "//*[@id=\"content\"]/form/div/div/input[2]").click()
        except NoSuchElementException as nee:
            self.logger.error(nee.msg)
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(nee.msg)
