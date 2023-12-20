from robot.libraries.BuiltIn import BuiltIn

from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class HomePage(BasicPageObject):
    """
    Page object for home page.
    """
    _HOME_PAGE_URL = BuiltIn().get_variable_value('${SERVER}')
    _BROWSER = BuiltIn().get_variable_value('${BROWSER}')
    _REMOTE_BROWSER_URL = BuiltIn().get_variable_value('${REMOTE_BROWSER_URL}')
    _USERNAME_INPUT_LOCATOR = r'id: user-name'
    _PASSWORD_INPUT_LOCATOR = r'id: password'
    _LOGIN_INPUT_LOCATOR = r'id: login-button'

    def open_home_page(self):
        self._webdriver.open_browser(url=self._HOME_PAGE_URL,
                                     browser=self._BROWSER,
                                     remote_url=self._REMOTE_BROWSER_URL,
                                     options='add_argument("--disable-dev-shm-usage")')

    def login(self, username, password):
        self._webdriver.input_text(self._USERNAME_INPUT_LOCATOR, username)
        self._webdriver.input_text(self._PASSWORD_INPUT_LOCATOR, password)
        self._webdriver.click_button(self._LOGIN_INPUT_LOCATOR)
