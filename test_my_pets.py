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
        name = browser.find_element_by_name('name')
        name.send_keys("Бинго")
        name = browser.find_element_by_name('age')
        name.send_keys("2")
        name = browser.find_element_by_name('sex')
        name.send_keys("M")
        conf = browser.find_element_by_css_selector("button").click()
        time.sleep(2)
        good_text = browser.find_element_by_css_selector(".notification.is-success").text
        print(good_text)

        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Сообщение Успех отсутствует"
        assert good_text == "Успех.", f"Неверный текст: {good_text}"
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Успех"
