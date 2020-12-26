from .pages.catalog_page import CatalogPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"

class TestCatalogPage:
    def test_guest_can_add_product_to_basket_from_catalog_page(self, browser):
        # Arrange
        page = CatalogPage(browser, link)
        page.open()
        # Act
        page.add_product_to_basket_from_catalog_page()
        # Assert
        page.is_product_added_to_basket()

    def test_go_to_next_catalog_page(self, browser):
        # Arrange
        page = CatalogPage(browser, link)
        page.open()
        # Act
        page.go_to_next_catalog_page()
        # Assert
        page.should_be_next_catalog_page_link()