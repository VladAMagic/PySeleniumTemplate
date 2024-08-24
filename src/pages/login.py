import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from src.pages.base import PageBase, Locator


class LoginPage(PageBase):
    url: str = "/signin"
    username_selector = Locator(By.XPATH, '//*[@id="username"]//input')
    password_selector = Locator(By.XPATH, '//*[@id="password"]//input')
    login_button = Locator(By.ID, "login-btn")
    login_error = Locator(By.XPATH, '//h3[@class="api-error"]')

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.wait.until(expected_conditions.url_contains(self.url))

    def fill_login(self, username: str = "demouser\n", password: str = "testingisfun99\n"):
        self.driver.find_element(*self.username_selector).is_displayed()
        self.driver.find_element(*self.username_selector).send_keys(username)
        self.driver.find_element(*self.password_selector).is_displayed()
        self.driver.find_element(*self.password_selector).send_keys(password)

    def submit_login(self):
        self.driver.find_element(*self.login_button).is_displayed()
        self.driver.find_element(*self.login_button).click()