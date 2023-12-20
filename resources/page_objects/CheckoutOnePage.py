from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class CheckoutOnePage(BasicPageObject):
    """
    Page object for checkout step one page.
    """

    _FIRST_NAME_INPUT = r'id: first-name'
    _LAST_NAME_INPUT = r'id: last-name'
    _POSTAL_CODE_INPUT = r'id: postal-code'
    _CONTINUE_BUTTON = r'id: continue'

    def input_name(self, first_name, last_name):
        self._webdriver.input_text(self._FIRST_NAME_INPUT, first_name)
        self._webdriver.input_text(self._LAST_NAME_INPUT, last_name)

    def input_zip_code(self, zip_code):
        self._webdriver.input_text(self._POSTAL_CODE_INPUT, zip_code)

    def click_on_continue(self):
        self._webdriver.click_button(self._CONTINUE_BUTTON)
