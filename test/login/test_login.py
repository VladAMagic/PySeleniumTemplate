from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.pages.home import HomePage
from test.base_test import BaseTest


class TestLogin(BaseTest):
    def test_default_login(self):
        login_page = HomePage(self.driver).open_login()
        login_page.fill_login()
        login_page.submit_login()
        assert self.wait.until(
            expected_conditions.url_contains('?signin=true'))

    def test_failed_login(self):
        login_page = HomePage(self.driver).open_login()
        login_page.fill_login("wrongUser\n", "wrongPassword\n")
        login_page.submit_login()
        assert self.driver.find_element(*login_page.login_error).is_displayed()
        assert self.driver.find_element(
            *login_page.login_error).text.__contains__("Invalid Username")
