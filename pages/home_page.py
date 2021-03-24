from pages.base_page import BasePage
from pages.locators import HomePageLocators, SearcPageLocators


class HomePage(BasePage):
    def get_all_prices_for_popular_products(self):
        return self.get_elements_present(*HomePageLocators.POPULAR_PRODUCT_PRICES)

    def put_search_field_and_click(self, text='dress'):
        search_field = self.get_element_present(*HomePageLocators.SEARCH_FIELD)
        search_button = self.get_element_present(*HomePageLocators.SEARCH_BUTTON)
        search_field.click()
        search_field.clear()
        search_field.send_keys(text)
        search_button.click()

    def is_displayed_result_search_text(self):
        search_result_text = self.get_element_present(*SearcPageLocators.SEARCH_RESULT).text
        assert 'РЕЗУЛЬТАТЫ ПОИСКА' == search_result_text, "Search result text isnt displayed"
