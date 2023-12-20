from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class ProductPage(BasicPageObject):
    """
    Page object for product page.
    """

    _CART_LOCATOR = r'id: shopping_cart_container'
    _ITEM_ADD_TO_CART_LOCATOR = (r'xpath: //div[contains(@class, "inventory_item_name") and contains(text(), "%")]'
                                 r'/ancestor::div[contains(@class, "inventory_item")]'
                                 r'//button[contains(@id, "add-to-cart")]')

    def add_product_to_chart(self, product_name):
        self._webdriver.click_button(self._ITEM_ADD_TO_CART_LOCATOR.replace('%', product_name))

    def click_on_cart(self):
        self._webdriver.click_element(self._CART_LOCATOR)
