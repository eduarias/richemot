from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class CheckoutCompletePage(BasicPageObject):
    """
    Page object for checkout complete page.
    """

    _COMPLETE_HEADER = r'xpath://h2[contains(@class, "complete-header")]'
    _COMPLETE_TEXT = r'xpath://div[contains(@class, "complete-text")]'

    def get_complete_header_text(self):
        return self._webdriver.get_text(self._COMPLETE_HEADER)

    def get_complete_text(self):
        return self._webdriver.get_text(self._COMPLETE_TEXT)
