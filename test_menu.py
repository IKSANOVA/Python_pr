from selenium.webdriver import Chrome
from functions import login


def test_menu():
    with Chrome() as browser:
        browser.maximize_window()
        browser.get("https://qastand.valhalla.pw/inputs")
        login(browser)
        menu_list = list()
        for element in browser.find_elements_by_css_selector('li a.navbar-item'):
            menu_list.append(element.text)
        assert menu_list == ['Поля ввода и кнопки', 'Мой питомец', 'О себе', 'Загрузка файла', 'Ожидание', 'Медленная загрузка', 'Модальные окна', 'Новая вкладка', 'iframe', 'Drag-and-drop']




