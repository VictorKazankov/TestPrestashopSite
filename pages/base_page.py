from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        assert "prestashop-automation" in self.browser.title

    def get_element_present(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def get_elements_present(self, how, what):
        try:
            elements = self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return elements