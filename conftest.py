import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from pages.search_page import SearchPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
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


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        br = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        br = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return br
    # capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": "89.0",
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": False
    #     }
    # }
    #
    # driver = webdriver.Remote(
    #     command_executor="http://192.168.99.100:4444/wd/hub",
    #     desired_capabilities=capabilities)

    # browser_name = request.config.getoption("--browser")
    #
    # if browser_name == "chrome":
    #     capability = {"browserName": "chrome",
    #                   "browserVersion": "89.0",
    #                   "selenoid:options": {
    #                       "enableVNC": True,
    #                       "enableVideo": True,
    #                       "enableLog": True
    #                   }
    #                   }
    #     br = webdriver.Remote(command_executor = "http://192.168.99.100:4444/wd/hub",
    #                           desired_capabilities=capability,
    #                           options=get_language_local_chrome(request))
    # elif browser_name == "firefox":
    #     capability = {"browserName": "firefox",
    #                   "browserVersion": "86.0",
    #                   "selenoid:options": {
    #                       "enableVNC": True,
    #                       "enableVideo": True,
    #                       "enableLog": True
    #                   }
    #                   }
    #     br = webdriver.Remote(command_executor = "http://192.168.99.100:4444/wd/hub",
    #                           desired_capabilities=capability,
    #                           browser_profile=get_language_local_firefox(request))
    # elif browser_name == "opera":
    #     capability = {"browserName": "opera",
    #                   "browserVersion": "74.0",
    #                   "selenoid:options": {
    #                       "enableVNC": True,
    #                       "enableVideo": True
    #                   }
    #                   }
    #     br = webdriver.Remote(command_executor = "http://192.168.99.100:4444/wd/hub",
    #                           desired_capabilities=capability)
    # else:
    #     raise ValueError("Unrecognized browser {}".format(browser_name))
    # return driver


@pytest.fixture(scope="function")
def browser(request):
    browser = change_browser(request)
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
