from selenium.webdriver import Chrome
import time

browser = Chrome()
browser.get('https://qastand.valhalla.pw/login')
print(f"{browser.current_url}")
email = browser.find_element_by_name('email')
email.send_keys('qa_test@test.ru')
password = browser.find_element_by_name('password')
password.send_keys('!QAZ2wsx')
buttom = browser.find_element_by_class_name('button.is-block.is-info.is-large.is-fullwidth')
buttom.click()
browser.close()
