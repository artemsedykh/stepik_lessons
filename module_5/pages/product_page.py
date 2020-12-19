from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()
    # переделать для фиксированного товара
    def should_be_same_product(self):
        success_label = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_LABEL)
        product_name = "Coders at Work"
        assert product_name in success_label.text, "Product was not added"
    # переделать для фиксированного товара
    def should_be_same_price(self):
        success_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_LABEL)
        product_price = "£19.99"
        assert product_price in success_price.text, f"Price is different: {success_price.text} vs {product_price}"


