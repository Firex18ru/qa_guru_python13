import pytest
from selene import browser
import time
@pytest.fixture(scope="session",autouse=True)
def browser_settings():
    browser.config.window_height = 768
    browser.config.window_width = 1024
#    time.sleep(3)
    yield
    browser.quit()
