from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functions import wait_until_clickable


def test_auth_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/login')
        print(f"{browser.current_url}")
        wait = WebDriverWait(browser, 10)
        wait_until_clickable(browser, By.NAME, 'email').send_keys("qa_test@test.ru")
        wait_until_clickable(browser, By.NAME, 'password').send_keys("!QAZ2wsx")
        wait_until_clickable(browser, By.CLASS_NAME, 'button')
        browser.find_element(By.CLASS_NAME, "button").click()


