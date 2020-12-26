from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_promotion_block(self):
        assert self.is_element_present(*MainPageLocators.PROMOTION_BLOCK), "Promotion block is not presented"
