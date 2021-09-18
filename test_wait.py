from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait

from functions import login, success_alert_is_present, wait_until_clickable, element_is_present, wait_until_visible


def test_wait():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/wait")
        browser.maximize_window()
        login(browser)
        wait = WebDriverWait(browser, 10)
        wait.until(ec.text_to_be_present_in_element((By.ID, "demo"), '100'))
        wait_until_clickable(browser, By.CSS_SELECTOR, '[onclick="check_value()"]').click()
        assert success_alert_is_present != "Успех!", "Неверный текст уведомления"


def test_wait_slow_load():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/slow_load")
        browser.maximize_window()
        login(browser)
        wait_until_clickable(browser, By.CSS_SELECTOR, '[id="text_input"]').send_keys('qa_test@test.ru')
        wait_until_clickable(browser, By.CSS_SELECTOR, '.button').click()
        element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success")
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Сообщение Успех отсутствует"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Сообщение Успех отсутствует"


def test_wait_profile():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/profile")
        browser.maximize_window()
        login(browser)
        wait = WebDriverWait(browser, 5)
        wait_until_clickable(browser, By.CSS_SELECTOR, '[href="/my_pet"]').click()
        wait.until(ec.url_to_be('https://qastand.valhalla.pw/my_pet'))
        browser.refresh()
        wait.until(title_is('Course Test Stand'))

