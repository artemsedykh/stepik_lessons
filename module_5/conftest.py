import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

AVAILABLE_LANGUAGES = ["ru", "en-GB", "es", "fr", "en"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Enter user language for tests")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language not in AVAILABLE_LANGUAGES:
        raise pytest.UsageError(f"'{language}' language code is out of scope!")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.user_language = language
    yield browser
    print("\nquit browser..")
    browser.quit()