from tests import LOG


def test_default_currency_displayed_in_popular_products(home_page):
    LOG.info("Run Default currency displayed in popular products test...")
    LOG.info("Getting prices from popular products")
    popular_product_prices_list = home_page.get_all_prices_for_popular_products()
    LOG.info("Verify all prices for popular products in current currency")
    home_page.all_product_prices_should_be_current_currency(popular_product_prices_list)


def test_usd_currency_displayed_in_popular_products(home_page):
    LOG.info("Run USD currency displayed in popular products test...")
    currency = 'USD'
    LOG.info("Set up USD currency")
    home_page.to_choose_currency(currency)
    LOG.info("Getting prices from popular products ")
    popular_product_prices_list = home_page.get_all_prices_for_popular_products()
    LOG.info("Verify all prices for popular products in USD")
    home_page.all_product_prices_should_be_current_currency(popular_product_prices_list)


def test_move_to_search_page(home_page):
    LOG.info("Run Move_to_search_page test...")
    word = 'dress'
    LOG.info("Put word to search field")
    home_page.put_search_field_and_click(word)
    LOG.info("Result text is displayed")
    home_page.is_displayed_result_search_text()
