from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from functions import login, element_is_present, wait_until_visible, wait_until_clickable2


def test_new_window():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/new_window_button")
        browser.maximize_window()
        login(browser)
        browser.implicitly_wait(10)
        wait_until_clickable2(browser, (By.CLASS_NAME, "button")).click()
        windows = browser.window_handles
        assert len(browser.window_handles) == 2
        browser.switch_to.window(windows[1])
        wait_until_clickable2(browser, (By.CLASS_NAME, "button")).click()
        browser.switch_to.alert
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.accept()
        assert len(browser.window_handles) == 1


def test_three_buttons():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/three_buttons")
        browser.maximize_window()
        login(browser)
        browser.find_element_by_css_selector('[onclick="confirm_func()"]').click()
        alert = browser.switch_to.alert
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.dismiss()
        assert element_is_present(browser, By.ID, "confirm_text"), "Сообщение Не запускаем отсутствует"


def test_iframe():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/iframe_page")
        browser.maximize_window()
        login(browser)
        browser.switch_to.frame(0)
        wait_until_visible(browser, (By.CSS_SELECTOR, 'button[onclick="alert_func()"]'))
        wait_until_visible(browser, (By.ID,'photo'))
        browser.find_element_by_css_selector('button[onclick="alert_func()"]').click()
        alert = browser.switch_to.alert
        alert = WebDriverWait(browser, 5).until(ec.alert_is_present())
        alert.accept()
        browser.switch_to.default_content()


def test_drag_and_drop():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/drag_and_drop_page")
        browser.maximize_window()
        login(browser)
        browser.implicitly_wait(10)
        el_to_drag = wait_until_clickable2(browser, (By.ID, "draggable"))
        el_to_drop = wait_until_clickable2(browser, (By.ID, "droppable"))
        ActionChains(browser).drag_and_drop(el_to_drag, el_to_drop).perform()
        assert element_is_present(browser, By.ID, "droppable"), "Успех"







