from selenium.webdriver.common.by import By


class HomePageLocators:
    POPULAR_PRODUCT_PRICES = (By.CLASS_NAME, "price")
    CURRENCY_DROPBOX = (By.XPATH, "//div[@class='currency-selector dropdown js-dropdown open']/a")