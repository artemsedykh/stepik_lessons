from .base_page import BasePage
from .locators import CatalogPageLocators

PRODUCT_NAME = "The shellcoder's handbook"
PRODUCT_PRICE = "£9.99"


class CatalogPage(BasePage):
    def product_index_in_catalog(self):
        products = self.browser.find_elements(*CatalogPageLocators.PRODUCT_DESCRIPTIONS)
        product_texts = [item.text for item in products]
        if PRODUCT_NAME in product_texts:
            return product_texts.index(PRODUCT_NAME)
        else:
            return -1

    def add_product_to_basket_from_catalog_page(self):
        add_to_basket_btns = self.browser.find_elements(*CatalogPageLocators.ADD_TO_BASKET_BTNS)
        product_index = self.product_index_in_catalog()
        if product_index != -1:
            add_to_basket_btns[product_index].click()
        else:
            print("Product was not found")

    def is_product_added_to_basket(self):
        assert self.is_element_present(*CatalogPageLocators.ADDED_TO_BASKET_LABEL), "no label"

    def should_be_same_product_as_added_to_basket(self):
        success_label = self.browser.find_element(*CatalogPageLocators.ADDED_TO_BASKET_LABEL)
        assert PRODUCT_NAME in success_label.text, "Product was not added"

    def should_be_same_price_as_added_to_basket(self):
        success_price = self.browser.find_element(*CatalogPageLocators.BASKET_PRICE_LABEL)
        assert PRODUCT_PRICE in success_price.text, f"Price is different: {success_price.text} vs {PRODUCT_PRICE}"

    def go_to_next_catalog_page(self):
        next_btn = self.browser.find_element(*CatalogPageLocators.NEXT_BTN)
        next_btn.click()

    def should_be_next_catalog_page_link(self):
        current_url = self.browser.current_url
        expected_url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/?page=2"
        assert current_url == expected_url, "Current URL is not expected for the next catalog page"
