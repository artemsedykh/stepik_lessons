from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Common methods
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    # Go to basket methods
    def go_to_basket_by_button_in_header(self):
        basket_btn = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_btn.click()

    # Login & auth methods
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    # Browse dropdown methods
    def should_be_browse_dropdown(self):
        assert self.is_element_present(*BasePageLocators.BROWSE_DROPDOWN_BTN), "There is now Browse dropdown"

    def expand_browse_dropdown_list(self):
        dropdown_btn = self.browser.find_element(*BasePageLocators.BROWSE_DROPDOWN_BTN)
        dropdown_btn.click()

    def should_be_expanded_browse_dropdown_list(self):
        assert len(self.browser.find_elements(*BasePageLocators.BROWSE_DROPDOWN_ELEMS)) > 0, "Browse dropdown list" \
                                                                                             "is not expanded"

    def should_be_link_text_in_browse_dropdown_list(self, link_text):
        dropdown_list = self.browser.find_elements(*BasePageLocators.BROWSE_DROPDOWN_ELEMS)
        dropdown_list_texts = [item.text.strip() for item in dropdown_list]
        assert link_text in dropdown_list_texts, f"Text {link_text} is not found in Browse dropdown"

    def click_on_element_from_dropdown_list(self, link_text):
        dropdown_list = self.browser.find_elements(*BasePageLocators.BROWSE_DROPDOWN_ELEMS)
        dropdown_list_texts = [item.text.strip() for item in dropdown_list]
        dropdown_list[dropdown_list_texts.index(link_text)].click()

    def should_be_correct_url_after_click_on_browse_dropdown_list(self, url):
        assert url in self.browser.current_url, "URL is incorrect"
