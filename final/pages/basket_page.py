from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_items_are_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "basket items are not present"

    def basket_items_are_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket items are present"

    def basket_empty_text_is_present(self):
        basket_is_empty_label = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_LABEL)
        exp_basket_is_empty_text = "Your basket is empty."
        assert exp_basket_is_empty_text in basket_is_empty_label.text, "no empty basket text is present"
