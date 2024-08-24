from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test.base_test import BaseTest


class PageBase:
    driver: webdriver
    wait: WebDriverWait

    def __init__(self, driver: webdriver):
        self.driver: webdriver = driver
        self.wait: WebDriverWait = BaseTest().get_wait(driver)

class Locator:
    def __new__(cls, by: By, value: str):
        return by, value