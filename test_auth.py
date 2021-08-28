from selenium.webdriver import Chrome


def test_auth_page():
    with Chrome() as browser:
        browser.get('https://qastand.valhalla.pw/login')
        print(f"{browser.current_url}")
        email = browser.find_element_by_name('email')
        email.send_keys('qa_test@test.ru')
        password = browser.find_element_by_name('password')
        password.send_keys('!QAZ2wsx')
        buttom = browser.find_element_by_class_name('button')
        buttom.click()


