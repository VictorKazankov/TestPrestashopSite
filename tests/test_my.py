from time import sleep


def test_currency_prices_correspond_established_in_populat_products(home_page):
    popular_product_prices_list = home_page.get_all_prices_for_popular_products()
    home_page.all_prices_are_current_currency(popular_product_prices_list)
    pass
