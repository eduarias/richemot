from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class CheckoutTwoPage(BasicPageObject):
    """
    Page object for checkout step two page.
    """

    _FINISH_BUTTON = r'id: finish'

    def click_on_finish(self):
        self._webdriver.click_button(self._FINISH_BUTTON)
