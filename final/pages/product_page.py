from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def is_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "no label"

    def is_not_product_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is presented, but should not"

    def is_success_message_disappeared_after_adding_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is not disappeared"
