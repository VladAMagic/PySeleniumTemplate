from selenium.webdriver.support import expected_conditions
from src.data.factory.user_fac import create_default_user
from src.pages.home import HomePage
from test.base_test import BaseTest


class TestHomePage(BaseTest):
    def test_login_button_is_displayed(self):
        homepage = HomePage(self.driver)
        self.driver.find_element(*homepage.signin_button).is_displayed()
