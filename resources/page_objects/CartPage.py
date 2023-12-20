from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class CartPage(BasicPageObject):
    """
    Page object for cart page.
    """

    _CHECKOUT_BUTTON = r'id: checkout'

    def click_on_checkout(self):
        self._webdriver.click_button(self._CHECKOUT_BUTTON)
