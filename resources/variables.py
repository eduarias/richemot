import os

import dotenv

dotenv.load_dotenv()

BROWSER = os.getenv('BROWSER', 'chrome')
REMOTE_BROWSER_URL = os.getenv('REMOTE_BROWSER_URL', False)
SERVER = os.getenv("SERVER", 'https://www.saucedemo.com')

VALID_USERNAME = os.getenv('VALID_USERNAME', 'standard_user')
VALID_PASSWORD = os.getenv('VALID_PASSWORD', 'secret_sauce')
