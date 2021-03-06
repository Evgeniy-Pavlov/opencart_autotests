import pytest
import os
from selenium import webdriver
import logging
import allure

mydir = os.getcwd().replace('\\', '/')
path = "tests/logs"
try:
    os.mkdir(mydir + path)
except OSError:
    print("Директория скорее всего уже существует")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests",
                     choices=["chrome", "firefox", "opera", "edge"])
    parser.addoption("--browser_version", default="96.0", help="Browser version to run tests",
                     choices=["95.0", "96.0", "94.0", "81.0", "82.0"])
    parser.addoption(
        "--filepath", default=os.path.expanduser("~/Downloads/drivers"), help="Root folder for drivers")
    parser.addoption(
        "--ext", default="", help="If you use windows pass .exe")
    parser.addoption(
        "--headless", action="store_true", help="To run browser headless")
    parser.addoption(
        "--url", action="store", default="https://demo.opencart.com/", type=str, help='Default url')
    parser.addoption(
        "--executor", action="store", default="192.168.56.1")
    parser.addoption(
        "--remote", action="store", default="True", help='To run remotely set True, set False to run locally.')


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    executor = request.config.getoption("--executor")
    remote = request.config.getoption('--remote')
    capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "name": "Evgeniy",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    if remote == "True":
        driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                                  desired_capabilities=capabilities)
        driver.implicitly_wait(2)
        driver.maximize_window()
        request.addfinalizer(driver.quit)
        return driver
    elif remote == "False":
        driver = None
        filepath = request.config.getoption("--filepath")
        browser_call = request.config.getoption("--browser")
        headless_mode = request.config.getoption("--headless")
        _ext = request.config.getoption("--ext")
        test_name = request.node.name
        logging.info("Tests {} started".format(test_name))
        if browser_call == "chrome":
            options = webdriver.ChromeOptions()
            options.headless = headless_mode
            driver = webdriver.Chrome(executable_path=f"{filepath}/chromedriver{_ext}", options=options)
        elif browser_call == "firefox":
            options = webdriver.FirefoxOptions()
            options.headless = headless_mode
            driver = webdriver.Firefox(executable_path=f"{filepath}/geckodriver{_ext}", options=options)
        elif browser_call == "edge":
            driver = webdriver.Edge(executable_path=f"{filepath}/msedgedriver{_ext}")
        elif browser_call == "opera":
            driver = webdriver.Opera(executable_path=f"{filepath}/operadriver_win64/operadriver{_ext}")

        def final():
            allure.attach(body=capabilities, attachment_type=allure.attachment_type.JSON, name='capabilities')
            driver.quit()

        request.addfinalizer(final)
        return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode):
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture
def url_call(request):
    url = request.config.getoption("--url")
    return url
