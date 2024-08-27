from selenium.webdriver.support import expected_conditions
from src.data.factory.user_fac import create_default_user
from src.pages.home import HomePage
from test.base_test import BaseTest


class TestLogin(BaseTest):
    def test_default_login(self):
        default_user = create_default_user()
        login_page = HomePage(self.driver).open_login()
        login_page.fill_login(default_user)
        login_page.submit_login()
        assert self.wait.until(
            expected_conditions.url_contains('?signin=true'))

    def test_failed_login(self):
        default_user = create_default_user(
            {"username": "wrongUser\n", "password": "wrongPassword\n"})
        login_page = HomePage(self.driver).open_login()
        login_page.fill_login(default_user)
        login_page.submit_login()
        assert self.driver.find_element(*login_page.login_error).is_displayed()
        assert self.driver.find_element(
            *login_page.login_error).text.__contains__("Invalid Username")
