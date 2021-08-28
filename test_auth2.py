import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login
from functions import element_is_present


def test_inputs_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/inputs")
        browser.maximize_window()
        login(browser)
        name = browser.find_element_by_name('test')
        name.send_keys("Проверка")
        button = browser.find_element_by_css_selector("[name='test'] + button").click()
        welcome_text = browser.find_element_by_css_selector(".notification.is-success").text
        print(welcome_text)

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Сообщение Верно отсутствует"
        assert welcome_text == "Верно", f"Неверный приветственный текст: {welcome_text}"
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Верно"
