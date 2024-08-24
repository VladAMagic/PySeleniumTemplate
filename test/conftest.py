import pytest
from selenium.webdriver.chrome.options import Options

class GlobalSetup:
    @pytest.fixture(scope="session", autouse=True)
    def global_setup(self):
        print("global setup")
        yield
        print("global teardown")

    @pytest.fixture(scope="session")
    def chrome_options(self) -> Options:
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--start-maximized")
        return chrome_options

def pytest_configure(config):
    global_setup = GlobalSetup()
    config.pluginmanager.register(global_setup)