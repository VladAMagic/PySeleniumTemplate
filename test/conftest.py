import pytest
from selenium.webdriver.chrome.options import Options


class GlobalSetup:
    @pytest.fixture(scope="session", autouse=True)
    def global_setup(self):
        print("global setup")
        yield
        print("global teardown")


def pytest_configure(config):
    global_setup = GlobalSetup()
    config.pluginmanager.register(global_setup)
