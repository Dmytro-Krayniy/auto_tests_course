from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alertinner > p > strong')


class MainPageLocators:
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.btn-primary')
