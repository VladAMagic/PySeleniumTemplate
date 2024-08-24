from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.pages.base import PageBase, Locator
from src.pages.login import LoginPage


class HomePage(PageBase):
    url: str = "https://www.bstackdemo.com/"
    signin_button = Locator(By.ID, "signin")

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait.until(expected_conditions.url_contains(self.url))

    def open_login(self) -> LoginPage:
        self.driver.find_element(*self.signin_button).is_displayed()
        self.driver.find_element(*self.signin_button).click()
        return LoginPage(self.driver)