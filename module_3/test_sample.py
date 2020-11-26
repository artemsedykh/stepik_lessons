#--------------------------------------------------------------------------------------------------------------------
# Тестовый сценарий 2.2.1 - Успешный вход под существующей учётной записью
# Шаги | Ожидаемый результат
# 1. Перейти по URL: http://selenium1py.pythonanywhere.com/ru/ | Страница открылась
# 2. Нажать на кнопку Войти или зарегистрироваться | Произошёл переход на страницу авторизации/регистрации
# 3. В блоке Войти в поле Адрес электронной почты ввести значение utest@utest.ru | Поле есть, значение удалось ввести
# 4. В блоке Войти в поле Пароль ввести значение Qwerty123! | Поле есть, значение удалось ввести
# 5. Нажать на кнопку Войти | Появилось сообщение об успешной авторизации
#--------------------------------------------------------------------------------------------------------------------

from selenium import webdriver
import time

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

search_login_link_locator = "#login_link"
search_login_username_locator = "#id_login-username"
search_login_password_locator = "#id_login-password"
search_login_button_locator = "button.btn.btn-lg"
search_message_locator = "div.alertinner"

def test_login_successful():
    #Data
    username = "utest@utest.ru"
    password = "Qwerty123!"

    successful_message = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        login_link = browser.find_element_by_css_selector(search_login_link_locator)
        login_link.click()

        # Act
        login_username = browser.find_element_by_css_selector(search_login_username_locator)
        login_username.send_keys(username)

        login_pass = browser.find_element_by_css_selector(search_login_password_locator)
        login_pass.send_keys(password)

        login_button = browser.find_element_by_css_selector(search_login_button_locator)
        login_button.click()

        # Assert
        message = browser.find_element_by_css_selector(search_message_locator)
        message_text = message.text

        assert successful_message in message_text, "Login unsuccessful"

    finally:
        time.sleep(5)
        browser.quit()

test_login_successful()