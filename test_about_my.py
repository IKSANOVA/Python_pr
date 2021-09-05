import os
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from functions import login, element_is_present


def test_about_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/about")
        browser.maximize_window()
        login(browser)
        name = browser.find_element_by_name('name').send_keys("Лилия")
        iks = browser.find_element_by_name('surname').send_keys("Иксанова")
        checkbox = browser.find_element_by_id("age1")
        assert checkbox.get_attribute("checked"), "Чекбокс включен по умолчанию"
        browser.find_element_by_id("age2").click()
        browser.find_element_by_id("age2").click()
        browser.find_element_by_id("lang1").click()
        browser.find_element_by_id("lang4").click()
        element = browser.find_element(By.NAME, "lvl")
        select = Select(element)
        select.select_by_index(4)
        # browser.find_element_by_css_selector("button.is-block").click()
        browser.find_element_by_name('surname').send_keys("Keys.ENTER")
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Успех."


def test_file_page():
    with Chrome() as browser:
        browser.get("https://qastand.valhalla.pw/upload_file")
        browser.maximize_window()
        login(browser)
        element_for_upload = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
        element_for_upload.send_keys(os.path.join(os.getcwd(), 'resources', 'Giraffe.jpg'))
        browser.find_element_by_css_selector('[type="submit"]').click()
        assert element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Успех присутствует"
        browser.refresh()
        assert not element_is_present(browser, By.CSS_SELECTOR, ".notification.is-success"), "Успех отсутствует"

        
