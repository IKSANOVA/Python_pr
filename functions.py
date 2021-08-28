from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def login(browser):
    email = browser.find_element(By.NAME, "email")
    email.send_keys("qa_test@test.ru")
    password = browser.find_element(By.NAME, "password")
    password.send_keys("!QAZ2wsx")
    browser.find_element(By.CLASS_NAME, "button").click()


def element_is_present(browser, by, value):
    try:
        browser.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

#
# def chek_menu(browser, by, value):
#     for browser.{find_elements(by, value)}:
#             if value == "пельмени":
#                 print("Я не ем пельмени!")
#                 break
#             print("Отлично, вкусные " + food)
#         else:
#             print("Хорошо, что не было пельменей!")