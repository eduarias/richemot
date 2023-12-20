from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from faker import Faker

from page_objects.HomePage import HomePage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.CheckoutOnePage import CheckoutOnePage
from page_objects.CheckoutTwoPage import CheckoutTwoPage
from page_objects.CheckoutCompletePage import CheckoutCompletePage


@library(scope='GLOBAL')
class Service(object):
    """
    Class that contains functional keywords .
    """

    def __init__(self):
        self._homepage = HomePage()
        self._product = ProductPage()
        self._cart = CartPage()
        self._checkout_one = CheckoutOnePage()
        self._checkout_two = CheckoutTwoPage()
        self._checkout_complete = CheckoutCompletePage()
        self.fake = Faker()

    @keyword("Open Home Page and Login")
    def open_home_page(self):
        self._homepage.open_home_page()
        self._homepage.login(BuiltIn().get_variable_value('${VALID_USERNAME}'),
                             BuiltIn().get_variable_value('${VALID_PASSWORD}'))

    @keyword('Added "${product_name}" To The Cart Ang Go To Cart Page')
    def add_product_to_the_cart_by_name(self, product_name):
        self._product.add_product_to_chart(product_name)
        self._product.click_on_cart()

    @keyword('Checking Out The Products On The Cart')
    def checking_out_products(self):
        self._cart.click_on_checkout()

    @keyword('Enter Checkout User Information')
    def enter_valid_chekout_user_information(self):
        self._checkout_one.input_name(self.fake.first_name(), self.fake.last_name())
        self._checkout_one.input_zip_code(self.fake.postcode())
        self._checkout_one.click_on_continue()

    @keyword('Finish Checkout Validation Information')
    def finish_checkout_validation(self):
        self._checkout_two.click_on_finish()

    @keyword('Order Text And Header Should Show Successful Message')
    def order_should_be_successful(self):
        BuiltIn().should_be_equal(self._checkout_complete.get_complete_header_text(),
                                  "Thank you for your order!",
                                  msg="Confirmation header not correct")
        BuiltIn().should_be_equal(self._checkout_complete.get_complete_text(),
                                  "Your order has been dispatched, "
                                  "and will arrive just as fast as the pony can get there!",
                                  msg="Confirmation text not correct")
        self._checkout_complete.capture_screenshot_with_random_name()
