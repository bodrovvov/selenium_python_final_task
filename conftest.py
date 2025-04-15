import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language:")

@pytest.fixture()
def wait(browser):
    return WebDriverWait(browser, 30)

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()