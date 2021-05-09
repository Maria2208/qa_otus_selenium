from config import Credentials
from pageObject.pages import *
import waits


def test_title(browser, base_url):
    """Проверка заголовка на главной странице"""
    browser.get(base_url)
    assert waits.wait_title("Your Store", browser)


def test_text_in_search_placeholder(browser, base_url):
    """Проверка текста в плейсхолдере поиска"""
    browser.get(base_url)
    search_input = waits.wait_element(CommonLocators.SEARCH_INPUT, browser).get_attribute("placeholder")
    assert search_input == "Search"


def test_length_of_products_list(browser, base_url):
    """Проверка, что на странице присутсвует как минимум одна карточка с товаром"""
    browser.get(f"{base_url}index.php?route=product/category&path=20")
    products_list = waits.wait_elements(ProductsLocators.PRODUCTS_LIST, browser)
    assert len(products_list) > 0


def test_success_text(browser, base_url):
    """Проверка появления алерта после нажатия кнопки обмена"""
    browser.get(f"{base_url}index.php?route=product/category&path=20")
    waits.wait_element(ProductsLocators.EXCHANGE_BTN, browser).click()
    alert_success = waits.wait_element(ProductsLocators.ALERT_SUCCESS, browser)
    assert "Success: You have added" in alert_success.text


def test_header_in_review(browser, base_url):
    """Проверка текста подзаголовка на вкладке review"""
    browser.get(f"{base_url}index.php?route=product/product&path=57&product_id=49")
    waits.wait_element(ProductsLocators.TAB_REVIEW, browser).click()
    header = waits.wait_element(ProductsLocators.REVIEW_HEADER, browser)
    assert header.text == "Write a review"


def test_register_account_button(browser, base_url):
    """Проверка текста заголовка страницы после клика на кнопку Continue"""
    browser.get(f"{base_url}index.php?route=account/login")
    waits.wait_element(LoginLocators.REGISTER_BTN, browser).click()
    assert waits.wait_title("Register Account", browser)


def test_login_button(browser, base_url):
    """Проверка текста алерта после клика на кнопку Login, если введены неверные лог/пасс"""
    browser.get(f"{base_url}index.php?route=account/login")
    waits.wait_element(LoginLocators.LOGIN_BTN, browser).click()
    alert = waits.wait_element(LoginLocators.ALERT_MSG, browser)
    assert "Warning: No match for E-Mail Address and/or Password" in alert.text


def test_check_header_after_login_admin_pass(browser, base_url):
    """Проверка текста заголовка страницы после авторизации в админке"""
    browser.get(f"{base_url}admin/")
    waits.wait_element(AdminLocators.LOGIN_INPUT, browser).send_keys(Credentials.LOGIN)
    waits.wait_element(AdminLocators.PASSWORD_INPUT, browser).send_keys(Credentials.PASSWORD)
    waits.wait_element(AdminLocators.LOGIN_BTN, browser).click()
    assert waits.wait_title("Dashboard", browser)


def test_check_input_after_click_forgotten_password(browser, base_url):
    """Проверка наличия инпута для ввода email после клика на кнопку Forgotten Password"""
    browser.get(f"{base_url}admin/")
    waits.wait_element(AdminLocators.FORGOTTEN_PASSWORD_BTN, browser).click()
    email_input = waits.wait_element(PasswordRecoveryLocators.EMAIL_INPUT, browser).get_attribute("placeholder")
    assert email_input == "E-Mail Address"
