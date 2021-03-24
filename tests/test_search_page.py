import pytest


def test_count_search_result_products(search_page):
    search_page.is_displayed_count_products_text()
    search_page.count_result_products_should_equal_total_products()


def test_all_prices_results_in_usd(search_page):
    currency = 'USD'
    search_page.to_choose_currency(currency)
    price_list = search_page.get_all_prices_for_search_results()
    search_page.all_product_prices_should_be_current_currency(price_list)


@pytest.mark.xfail(reason="Sorting function works incorrect")
def test_sort_ascending_products(search_page):
    type_sorting_text = 'Цене: от высокой к низкой'
    search_page.to_sort_products(type_sorting_text)
    search_page.is_sorting_value_to_sorting_dropbox(type_sorting_text)
    search_page.products_should_be_ascending()


@pytest.mark.xfail(reason="Sorting function works incorrect")
def test_sort_descending_products(search_page):
    type_sorting_text = 'Цене: от низкой к высокой'
    search_page.to_sort_products(type_sorting_text)
    search_page.is_sorting_value_to_sorting_dropbox(type_sorting_text)
    search_page.products_should_be_descending()


def test_present_percentage_discount(search_page):
    discount_products_list = search_page.get_discount_products()
    search_page.is_displayed_5_percentages_discount(discount_products_list)
    search_page.is_displayed_20_percentages_discount(discount_products_list)


def test_verify_correct_calculate_discount(search_page):
    regular_price = search_page.get_regular_price()
    discount_price = search_page.get_discount_price()
    discount_percentage = search_page.get_discount_percentage()
    assert discount_percentage == int(100 - discount_price / regular_price * 100)
