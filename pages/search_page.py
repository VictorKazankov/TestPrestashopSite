from time import sleep

from pages.base_page import BasePage
from pages.locators import SearcPageLocators


class SearchPage(BasePage):

    def is_displayed_count_products_text(self):
        result_search_products = self.get_element_present(*SearcPageLocators.SEARCH_RESULT_COUNT_PRODUCTS)
        # need text is existed
        assert 'Товаров:' in result_search_products.text, "Products: text isn't displayes"

    def count_result_products_should_equal_total_products(self):
        count_all_results = self.get_element_present(*SearcPageLocators.ALL_PRODUCTS)
        # cut only count of result
        all_count_products = [s for s in count_all_results.text if s.isdigit()][-1]
        result_search_products = self.get_element_present(*SearcPageLocators.SEARCH_RESULT_COUNT_PRODUCTS)
        # cut count products from search result
        count_search_results = [s for s in result_search_products.text if s.isdigit()][0]
        # compare found results with count total
        assert count_search_results == all_count_products, "Count search result not equal total result"

    def get_all_prices_for_search_results(self):
        return self.get_elements_present(*SearcPageLocators.SEARCH_PRODUCT_PRICES)

    def search_result_should_be_usd(self, prices):
        self.all_product_prices_should_be_current_currency(prices)

    def to_sort_products(self, type_sorting):
        select_sort_dropbox = self.get_element_present(*SearcPageLocators.SELECT_SORT_DROPBOX)
        if type_sorting not in select_sort_dropbox.text:
            select_sort_dropbox.click()
            select_sort_list = self.get_elements_present(*SearcPageLocators.SELECT_SORT_LIST)
            [element.click() for element in select_sort_list if element.text == type_sorting]
            sleep(0.5)

    def is_sorting_value_to_sorting_dropbox(self, value):
        select_sort_dropbox = self.get_element_present(*SearcPageLocators.SELECT_SORT_DROPBOX)
        assert value in select_sort_dropbox.text

    def products_should_be_ascending(self):
        prices = self.get_products_prices_text()
        assert prices == sorted(prices, reverse=True)

    def products_should_be_descending(self):
        prices = self.get_products_prices_text()
        assert prices == sorted(prices, reverse=False)

    def get_products_prices_text(self):
        list_prices = self.get_all_prices_for_search_results()
        prices = list(map(lambda i: i.text, list_prices))
        return prices

    def get_discount_products(self):
        return self.get_elements_present(*SearcPageLocators.DISCOUNT_PRODUCTS)

    def is_displayed_5_percentages_discount(self, products_list):
        discount = list(map(lambda i: i.text, products_list))
        assert '-5%' in discount

    def is_displayed_20_percentages_discount(self, products_list):
        discount = list(map(lambda i: i.text, products_list))
        assert '-20%' in discount

    def get_regular_price(self):
        regular_price = self.get_element_present(*SearcPageLocators.REGULAR_PRICE_PRODUCT)
        return float(regular_price.text[:-2].replace(',', '.'))

    def get_discount_price(self):
        discount_price = self.get_element_present(*SearcPageLocators.DISCOUNT_PRICE_PRODUCT)
        return float(discount_price.text[:-2].replace(',', '.'))

    def get_discount_percentage(self):
        discount_percentage = self.get_element_present(*SearcPageLocators.DISCOUNT_PERCENTAGE_PRODUCT)
        return abs(int(discount_percentage.text[:-1]))
