import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from pages.search_page import SearchPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="ru")


def get_language_local_chrome(request):
    local = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': local})
    return options


def get_language_local_firefox(request):
    local = request.config.getoption("--language")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", local)
    return fp


capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "89.0",
        "config:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True
        }
    },
    {
        "browserName": "firefox",
        "browserVersion": "86.0",
        "config:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True
        }
    },
    {
        "browserName": "opera",
        "browserVersion": "74.0",
        "config:options": {
            "enableVNC": True,
            "enableVideo": False,
            "enableLog": True
        }
    }
]


def change_browser(request):
    driver = webdriver.Remote(
        command_executor="http://192.168.99.101:4444/wd/hub",
        desired_capabilities=request)
    return driver


@pytest.fixture(scope="session", params=capabilities, ids=["chrome", "firefox", ""])
def browser(request):
    browser = change_browser(request.param)
    yield browser
    browser.quit()


@pytest.fixture()
def home_page(browser):
    home_page_url = "http://prestashop-automation.qatestlab.com.ua"
    home_page = HomePage(browser, home_page_url)
    home_page.open()
    return home_page


@pytest.fixture()
def search_page(browser, home_page):
    home_page.put_search_field_and_click()
    search_page = SearchPage(browser, browser.current_url)
    return search_page
