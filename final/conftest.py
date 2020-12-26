import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from datetime import datetime

AVAILABLE_LANGUAGES = ["ru", "en-GB", "es", "fr"]
AVAILABLE_BROWSERS = ["chrome", "firefox"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Enter user language for tests")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language not in AVAILABLE_LANGUAGES:
        raise pytest.UsageError(f"'{language}' language code is out of scope!")

    browser_name = request.config.getoption("browser_name")
    if browser_name not in AVAILABLE_BROWSERS:
        raise pytest.UsageError(f"'{browser_name}' browser is out of scope!")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)

    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.user_language = language
    yield browser
    # now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # browser.save_screenshot('screenshot-%s.png' % now)
    print("\nquit browser..")
    browser.quit()
