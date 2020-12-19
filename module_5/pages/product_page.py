from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_same_product_as_added_to_basket(self):
        success_label = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_LABEL)
        product_name = "Coders at Work"
        assert product_name in success_label.text, "Product was not added"

    def should_be_same_price_as_added_to_basket(self):
        success_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_LABEL)
        product_price = "£19.99"
        assert product_price in success_price.text, f"Price is different: {success_price.text} vs {product_price}"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def is_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "no label"

    def is_not_product_added_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is presented, but should not"

    def is_success_message_disappeared_after_adding_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_LABEL), "is not disappeared"
