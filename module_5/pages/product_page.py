from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_same_product(self):
        success_label = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_LABEL)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text in success_label.text, "Product was not added"

    def should_be_same_price(self):
        success_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_LABEL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text in success_price.text, "Price is different"


