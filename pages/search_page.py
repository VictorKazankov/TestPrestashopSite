from pages.base_page import BasePage
from pages.locators import SearcPageLocators


class SearchPage(BasePage):

    def is_displayed_all_count_products(self):
        result_search_products = self.get_element_present(*SearcPageLocators.SEARCH_RESULT_COUNT_PRODUCTS)
        count_all_result = self.get_element_present(*SearcPageLocators.COUNT_ALL_PRODUCTS)
        # need text is existed
        assert 'Товаров:' in result_search_products.text, "Products: test isn't displayes"
        count_all_result = [s for s in count_all_result.text if s.isdigit()][-1]
        count_result = [s for s in result_search_products.text if s.isdigit()][0]
        # compare found results with count total
        assert count_result == count_all_result, "Count search result not equal total result"

    def get_all_prices_for_search_results(self):
        return self.get_elements_present(*SearcPageLocators.SEARCH_PRODUCT_PRICES)

    def search_result_should_be_usd(self, prices):
        self.all_product_prices_should_be_current_currency(prices)