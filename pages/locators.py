from selenium.webdriver.common.by import By


class GeneralLocators:
    CURRENCY_SELECTOR = (By.ID, "_desktop_currency_selector")
    CURRENCY_DROPBOX = (By.XPATH, "//span[@class='expand-more _gray-darker hidden-sm-down']")
    DROPDOWN_CURRENCY_LIST = (By.XPATH, "//ul[@class='dropdown-menu hidden-sm-down']/li")


class HomePageLocators:
    POPULAR_PRODUCT_PRICES = (By.CLASS_NAME, "price")
    SEARCH_FIELD = (By.NAME, "s")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class SearcPageLocators:
    SEARCH_RESULT = (By.XPATH, "//section[@id='main']/h2")
    SEARCH_RESULT_COUNT_PRODUCTS = (By.XPATH, "//div[@id='js-product-list-top']/div/p")
    COUNT_ALL_PRODUCTS = (By.CSS_SELECTOR, "div[class='col-md-4']")
    SEARCH_PRODUCT_PRICES = (By.CLASS_NAME, "price")
