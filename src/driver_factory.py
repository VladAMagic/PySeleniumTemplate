from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    def get_driver(self, browser) -> webdriver:
        match browser:
            case 'chrome':
                chrome_options = Options()
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument(
                    "--disable-search-engine-choice-screen")
                chrome_options.add_argument("--start-maximized")
                return webdriver.Chrome(chrome_options)
            case 'firefox':
                return webdriver.Firefox()
            case 'edge':
                return webdriver.Edge()
            case _:
                raise ValueError('Invalid browser name')
