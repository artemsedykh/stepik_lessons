from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"
BROWSE_DROPDOWN_URLS = {
    "All products": "http://selenium1py.pythonanywhere.com/en-gb/catalogue/",
    "Clothing": "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/clothing_1/",
    "Books": "http://selenium1py.pythonanywhere.com/en-gb/catalogue/category/books_2/",
    "Offers": "http://selenium1py.pythonanywhere.com/en-gb/offers/"
}

class TestMainPage:
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

    def test_quest_can_see_promotion_block(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        # Assert
        page.should_be_promotion_block()


@pytest.mark.login_guest
class TestLoginFromMainPage:
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
        login_page.should_be_login_url()

@pytest.mark.browse_dropdown
class TestBrowseDropdownOnMainPage:
    def test_browse_dropdown_should_be_on_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        # Assert
        page.should_be_browse_dropdown()

    def test_browse_dropdown_can_be_expanded(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.expand_browse_dropdown_list()
        # Assert
        page.should_be_expanded_browse_dropdown_list()

    @pytest.mark.parametrize('element', BROWSE_DROPDOWN_URLS.keys())
    def test_should_be_element_in_browse_dropdown(self, browser, element):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.expand_browse_dropdown_list()
        # Assert
        page.should_be_link_text_in_browse_dropdown_list(element)

    @pytest.mark.parametrize('element', BROWSE_DROPDOWN_URLS.keys())
    def test_should_be_correct_url_after_click_on_browse_dropdown_element(self, browser, element):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        # Act
        page.expand_browse_dropdown_list()
        page.click_on_element_from_dropdown_list(element)
        # Assert
        url = BROWSE_DROPDOWN_URLS[element]
        page.should_be_correct_url_after_click_on_browse_dropdown_list(url)
