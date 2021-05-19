import pytest
import os

from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions

DRIVERS = os.path.expanduser("~/Develop/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera", "safari"], default="safari")
    parser.addoption("--url", action="store", default="http://localhost/", help="This is request url")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(
            options=options,
            executable_path=f"{DRIVERS}/chromedriver"
        )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.headless = headless

        driver = webdriver.Firefox(
            options=options,
            executable_path=f"{DRIVERS}/geckodriver"
        )
    elif browser == "opera":
        options = OperaOptions()

        driver = webdriver.Opera(
            options=options,
            executable_path=f"{DRIVERS}/operadriver_mac64/operadriver"
        )
    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError("Driver not supported: {}".format(browser))

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
