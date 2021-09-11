from webbrowser import Chrome

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement


def login(browser):
    wait = WebDriverWait(browser, 10)
    wait_until_clickable(browser, By.NAME, 'email')
    browser.find_element(By.NAME, "email").send_keys("qa_test@test.ru")
    wait_until_clickable(browser, By.NAME, 'password')
    browser.find_element(By.NAME, "password").send_keys("!QAZ2wsx")
    wait_until_clickable(browser, By.CLASS_NAME, 'button')
    browser.find_element(By.CLASS_NAME, "button").click()


def wait_until_clickable(driver: Chrome, by: By, value: str, timeout: int = 5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable((by, value)))


def wait_until_present(driver: Chrome, by: By, value: str, timeout=5) -> WebElement:
    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located((by, value)))


def wait_until_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(ec.visibility_of_element_located(locator))


def element_is_present(browser: Chrome, by: By, value: str, timeout=10) -> bool:
    try:
        wait_until_visible(browser, (by, value), timeout)
        return True
    except TimeoutException:
        return False


def success_alert_is_present(driver: Chrome, timeout=5) -> bool:
    alert = WebDriverWait(driver, timeout).until(ec.alert_is_present())
    assert "Успех!" in alert.text
