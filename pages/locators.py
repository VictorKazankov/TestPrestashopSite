from selenium.webdriver.common.by import By


class GeneralLocators:
    CURRENCY_SELECTOR = (By.XPATH, "//div[@id='_desktop_currency_selector']/*/*[2]")
    CURRENCY_DROPBOX = (By.XPATH, "//span[@class='expand-more _gray-darker hidden-sm-down']")
    DROPDOWN_CURRENCY_LIST = (By.XPATH, "//ul[@class='dropdown-menu hidden-sm-down']/li")


class HomePageLocators:
    POPULAR_PRODUCT_PRICES = (By.CLASS_NAME, "price")
    SEARCH_FIELD = (By.NAME, "s")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class SearcPageLocators:
    SEARCH_RESULT = (By.XPATH, "//section[@id='main']/h2")
    SEARCH_RESULT_COUNT_PRODUCTS = (By.XPATH, "//div[@id='js-product-list-top']/div/p")
    ALL_PRODUCTS = (By.CSS_SELECTOR, "div[class='col-md-4']")
    SEARCH_PRODUCT_PRICES = (By.CLASS_NAME, "price")
    SELECT_SORT_DROPBOX = (By.CLASS_NAME, "select-title")
    SELECT_SORT_LIST = (By.XPATH, "//div[@class='dropdown-menu']/a")
    DISCOUNT_PRODUCTS = (By.CSS_SELECTOR, "div[class='products row'] [class='discount-percentage']")
    DISCOUNT_PERCENTAGE_PRODUCT = [By.XPATH, "//span[@class='discount-percentage']"]
    REGULAR_PRICE_PRODUCT = [By.XPATH, "//span[@class='discount-percentage']/preceding-sibling::*"]
    DISCOUNT_PRICE_PRODUCT = [By.XPATH, "//span[@class='discount-percentage']/following-sibling::*"]
