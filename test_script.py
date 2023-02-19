from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element(By.ID, 'book').click()


    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    # browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    # first_window = browser.window_handles[0]
    #
    # robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    # browser.execute_script('return arguments[0].scrollIntoView(true)', robot_checkbox)
    # robot_checkbox.click()
    # browser.find_element(By.ID, 'robotsRule').click()

    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.find_element(By.ID, "solve").click()

    # time.sleep(1)
    # alert = browser.switch_to.alert
    # alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
