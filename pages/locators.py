from selenium.webdriver.common.by import By


class HomePageLocators:
    POPULAR_PRODUCT_PRICES = (By.CLASS_NAME, "price")
    CURRENCY_SELECTOR = (By.ID, "_desktop_currency_selector")
