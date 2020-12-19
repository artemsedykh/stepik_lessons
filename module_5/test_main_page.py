from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_by_button_in_header()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.basket_items_are_not_present()
        basket_page.basket_empty_text_is_present()
