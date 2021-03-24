import pytest

from tests import LOG


def test_count_search_result_products(search_page):
    LOG.info("Run Count search result products test...")
    LOG.info("Verify display text with count products")
    search_page.is_displayed_count_products_text()
    LOG.info("Verify count of results equal total results")
    search_page.count_result_products_should_equal_total_products()


def test_all_prices_results_in_usd(search_page):
    LOG.info("Run All prices results in USD test...")
    currency = 'USD'
    LOG.info("Set up USD currency")
    search_page.to_choose_currency(currency)
    LOG.info("Getting product price list")
    price_list = search_page.get_all_prices_for_search_results()
    LOG.info("Verify all prices for popular products in USD")
    search_page.all_product_prices_should_be_current_currency(price_list)


@pytest.mark.xfail(reason="Sorting function works incorrect")
def test_sort_ascending_products(search_page):
    LOG.info("Run Sort acsending products test...")
    type_sorting_text = 'Цене: от высокой к низкой'
    LOG.info("Do sorting products")
    search_page.to_sort_products(type_sorting_text)
    LOG.info("Verify sorting value sets to dropbox")
    search_page.is_sorting_value_to_sorting_dropbox(type_sorting_text)
    LOG.info("Verify products are ascended")
    search_page.products_should_be_ascending()


@pytest.mark.xfail(reason="Sorting function works incorrect")
def test_sort_descending_products(search_page):
    LOG.info("Run Sort descending products test...")
    LOG.info("Do sorting products")
    type_sorting_text = 'Цене: от низкой к высокой'
    search_page.to_sort_products(type_sorting_text)
    LOG.info("Verify sorting value sets to dropbox")
    search_page.is_sorting_value_to_sorting_dropbox(type_sorting_text)
    LOG.info("Verify products are descended")
    search_page.products_should_be_descending()


def test_present_percentage_discount(search_page):
    LOG.info("Run Present percentage discount run...")
    LOG.info("Getting products with discount")
    discount_products_list = search_page.get_discount_products()
    LOG.info("Verify products with 5 percentages discount are displayed")
    search_page.is_displayed_5_percentages_discount(discount_products_list)
    LOG.info("Verify products with 20 percentages discount are displayed")
    search_page.is_displayed_20_percentages_discount(discount_products_list)


def test_verify_correct_calculate_discount(search_page):
    LOG.info("Run Verify correct calculate of discount...")
    LOG.info("Getting regular price")
    regular_price = search_page.get_regular_price()
    LOG.info("Getting discount price")
    discount_price = search_page.get_discount_price()
    LOG.info("Getting discount percentage")
    discount_percentage = search_page.get_discount_percentage()
    LOG.info("Verify discount calculate is correctly")
    assert discount_percentage == int(100 - discount_price / regular_price * 100)
