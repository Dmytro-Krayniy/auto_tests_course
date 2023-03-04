import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from .pages.main_page import MainPage

HOME_LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, HOME_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, HOME_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.last
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, HOME_LINK)
    page.open()
    # page.add_first_product_to_basket()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.any_product_is_not_in_basket()
    basket.should_be_basket_empty_message()
