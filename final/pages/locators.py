from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")
    BROWSE_DROPDOWN_BTN = (By.CSS_SELECTOR, "#browse > li > a")
    BROWSE_DROPDOWN_ELEMS = (By.CSS_SELECTOR, "#browse > li > ul a")


class MainPageLocators():
    PROMOTION_BLOCK = (By.CSS_SELECTOR, "#promotions")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_LABEL = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_PRICE_LABEL = (By.CSS_SELECTOR, ".alert-info p:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS_CHECK = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "div.register_form .btn")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_LABEL = (By.CSS_SELECTOR, "#content_inner > p")


class CatalogPageLocators():
    PRODUCT_DESCRIPTIONS = (By.CSS_SELECTOR, "section h3")
    ADD_TO_BASKET_BTNS = (By.CSS_SELECTOR, "section button")
    ADDED_TO_BASKET_LABEL = (By.CSS_SELECTOR, ".alert-success")
    BASKET_PRICE_LABEL = (By.CSS_SELECTOR, ".alert-info p:nth-child(1)")
    NEXT_BTN = (By.CSS_SELECTOR, "div li.next a")
