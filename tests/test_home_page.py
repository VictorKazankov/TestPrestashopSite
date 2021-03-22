def test_default_currency_displayed_in_popular_products(home_page):
    popular_product_prices_list = home_page.get_all_prices_for_popular_products()
    home_page.all_product_prices_should_be_current_currency(popular_product_prices_list)


def test_usd_currency_displayed_in_popular_products(home_page):
    currency = 'USD'
    home_page.to_choose_currency(currency)
    popular_product_prices_list = home_page.get_all_prices_for_popular_products()
    home_page.all_product_prices_should_be_current_currency(popular_product_prices_list)


def test_go_to_search_page(home_page):
    text = 'dress'
    home_page.put_search_field_and_click(text)
    home_page.is_displayed_result_search_text()
