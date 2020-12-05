# Data
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

add_to_cart_button_locator = ".btn-add-to-basket"

def test_add_to_basket_button_text(browser):
    # Data
    add_to_cart_button_text_by_lang = {
        "ru": "Добавить в корзину",
        "en-GB": "Add to basket",
        "fr": "Ajouter au panier",
        "es": "Añadir al carrito"
    }
    exp_language_code = browser.user_language
    exp_add_to_cart_button_text = add_to_cart_button_text_by_lang[exp_language_code]

    # Arrange
    browser.get(product_page_link)

    # Act
    add_to_cart_button = browser.find_element_by_css_selector(add_to_cart_button_locator)
    add_to_cart_button_text = add_to_cart_button.text

    # Assert
    assert add_to_cart_button_text == exp_add_to_cart_button_text, "Text on the button is different"