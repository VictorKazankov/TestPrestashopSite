def test_is_displayed_count_products_text(search_page):
    search_page.is_displayed_all_count_products()


def test_all_prices_results_in_usd(search_page):
    currency = 'USD'
    search_page.to_choose_currency(currency)
    price_list = search_page.get_all_prices_for_search_results()
    search_page.all_product_prices_should_be_current_currency(price_list)
