from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def get_all_prices_for_popular_products(self):
        return self.get_elements_present(*HomePageLocators.POPULAR_PRODUCT_PRICES)

    def all_prices_are_current_currency(self, list_prices):
        currency_dropbox = Select(self.get_element_present(*HomePageLocators.CURRENCY_DROPBOX))
        current_currency = currency_dropbox.first_selected_option
        for price in list_prices:
            price_text = price.text
            a = price_text[-1]
            pass

        pass