from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest, time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

class TestProductPage:

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.is_not_product_added_to_basket()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        # Assert
        page.is_not_product_added_to_basket()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.is_success_message_disappeared_after_adding_to_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.go_to_basket_by_button_in_header()
        basket_page = BasketPage(browser, browser.current_url)
        # Assert
        basket_page.basket_items_are_not_present()
        basket_page.basket_empty_text_is_present()

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.is_not_product_added_to_basket()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        # Assert
        page.is_product_added_to_basket()

