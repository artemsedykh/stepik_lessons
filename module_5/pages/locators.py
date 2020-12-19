from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_LABEL = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_PRICE_LABEL = (By.CSS_SELECTOR, ".alert-info p:nth-child(1)")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_LABEL = (By.CSS_SELECTOR, "#content_inner > p")