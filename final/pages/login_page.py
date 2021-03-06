from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' is not presented in current URL"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)

        pass_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        pass_input.send_keys(password)

        pass_check_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASS_CHECK)
        pass_check_input.send_keys(password)

        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        reg_btn.click()
