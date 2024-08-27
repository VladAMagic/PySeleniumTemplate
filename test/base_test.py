import time
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.driver_factory import DriverFactory
from src.utils.config_reader import read_config


class BaseTest:
    driver: WebDriver
    wait: WebDriverWait

    @pytest.fixture(autouse=True)
    def before_each(self):
        self.driver = DriverFactory().get_driver(read_config('WEBSITE', 'Browser'))
        website_url = read_config('WEBSITE', 'BaseUrl')
        # website_url = 'https://bstackdemo.com/'
        self.driver.get(website_url)
        self.get_wait(self.driver)
        time.sleep(3)
        yield
        if self.driver:
            self.driver.quit()
            self.driver = None

    def get_wait(self, driver: webdriver) -> WebDriverWait:
        driver.implicitly_wait(
            float(read_config('WEBSITE', 'ImplicitWaitTime')))
        self.wait = WebDriverWait(driver, float(
            read_config('WEBSITE', 'WaitTime')))
        return self.wait
