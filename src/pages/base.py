from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.base_test import BaseTest


class PageBase:
    driver: WebDriver
    wait: WebDriverWait

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = BaseTest().get_wait(driver)


class Locator:
    def __new__(cls, by: By, value: str):
        return by, value
