from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    def get_all_prices_for_popular_products(self):
        return self.get_elements_present(*HomePageLocators.POPULAR_PRODUCT_PRICES)

    def all_product_prices_should_be_current_currency(self, popular_product_prices_list):
        # get current currency icon
        current_currency_text = self.get_element_present(*HomePageLocators.CURRENCY_SELECTOR).text[:-2]
        current_currency_icon = current_currency_text[-1]
        # get currency icons for all popular product_objects and compare them with current currency icon
        currency_icons_list = list(map(lambda x: x.text[-1], popular_product_prices_list))
        for icon in currency_icons_list:
            assert icon == current_currency_icon
