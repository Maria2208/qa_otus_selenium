from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_title(title, driver, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        raise AssertionError("Ждала что title будет: '{}' но он был '{}'".format(title, driver.title))


def wait_element(selector, driver, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(selector))
    except TimeoutException:
        driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError("Не дождалась видимости элемента: {}".format(selector))


def wait_elements(selector, driver, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(selector))
    except TimeoutException:
        driver.save_screenshot("{}.png".format(driver.session_id))
        raise AssertionError("Не дождалась видимости элементов: {}".format(selector))
