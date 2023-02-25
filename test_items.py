import time

from selenium.webdriver.common.by import By


def test_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(30)
    assert basket_button, 'Button "Add to basket" not found'

