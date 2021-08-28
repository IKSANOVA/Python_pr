import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import login
from functions import element_is_present


def test_my_pets_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/my_pet")
        browser.maximize_window()
        login(browser)
        name = browser.find_element_by_name('pet')
        name.send_keys("Собака")
        conf = browser.find_element_by_css_selector("button").click()
        time.sleep(2)
        no_text = browser.find_element_by_css_selector(".notification.is-danger").text
        print(no_text)

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-danger"), "Сообщение Успех отсутствует"
        assert no_text == "Заполнены не все поля.", f"Неверный текст: {no_text}"
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Успех"
