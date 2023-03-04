from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def add_first_product_to_basket(self):
        button = self.browser.find_element(*MainPageLocators.FIRST_PRODUCT)
        button.click()
