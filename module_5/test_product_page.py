from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is presented, but should not"

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        # Assert
        assert page.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is presented, but should not"

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        # Assert
        assert page.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is not_disappeared"

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