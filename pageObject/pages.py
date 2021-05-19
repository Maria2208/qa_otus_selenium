from selenium.webdriver.common.by import By


class CommonLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, '#search .form-control.input-lg')


class LoginLocators:
    REGISTER_BTN = (By.CSS_SELECTOR, '.well a.btn.btn-primary')
    LOGIN_BTN = (By.CSS_SELECTOR, 'input.btn.btn-primary')
    ALERT_MSG = (By.CSS_SELECTOR, ".alert.alert-danger")


class AdminLocators:
    LOGIN_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    LOGIN_BTN = (By.CSS_SELECTOR, '.btn.btn-primary')
    FORGOTTEN_PASSWORD_BTN = (By.CSS_SELECTOR, '.help-block a')
    ALERT_AUTH_FAILED = (By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible')


class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")


class ProductsLocators:
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".product-thumb")
    EXCHANGE_BTN = (By.CSS_SELECTOR, '.button-group .fa.fa-exchange')
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    TAB_REVIEW = (By.CSS_SELECTOR, 'a[href = "#tab-review"]')
    REVIEW_HEADER = (By.CSS_SELECTOR, '.form-horizontal h2')
