from selenium.common.exceptions import NoSuchElementException

from pages.locators import GeneralLocators


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

    def to_choose_currency(self, currency):
        currency_dropbox = self.get_element_present(*GeneralLocators.CURRENCY_DROPBOX)
        currency_dropbox.click()
        dropdown_list = self.get_elements_present(*GeneralLocators.DROPDOWN_CURRENCY_LIST)
        currency_list = [element for element in dropdown_list if len(element.text) > 0]
        [element.click() for element in currency_list if currency in element.text]

    def all_product_prices_should_be_current_currency(self, prices_list):
        # get current currency icon
        current_currency_text = self.get_element_present(*GeneralLocators.CURRENCY_SELECTOR).text[:-2]
        current_currency_icon = current_currency_text[-1]
        # get currency icons for all product_objects and compare them with current currency icon
        currency_icons_list = list(map(lambda x: x.text[-1], prices_list))
        for icon in currency_icons_list:
            assert icon == current_currency_icon, "Product currency icon not equal current currency icon"
