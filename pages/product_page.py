import pytest

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    title = ''
    price = ''

    def add_product_to_basket(self):
        self.title = self.browser.find_element(*ProductPageLocators.TITLE).text
        self.price = self.browser.find_element(*ProductPageLocators.PRICE).text
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_product_title_in_the_basket(self, success_message):
        msgs = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        assert self.title + success_message == msgs[0].text,\
            f'Message "{msgs[0].text}" should be {self.title + success_message}'

    def check_basket_total_and_price(self):
        bt = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert bt == self.price, f'Basket total should be equal to product price. {bt} != {self.price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented'

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message does not disappear'

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            f'Not found success message for added product "{self.title}"'
