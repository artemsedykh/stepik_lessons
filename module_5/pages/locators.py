from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_LABEL = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_PRICE_LABEL = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")