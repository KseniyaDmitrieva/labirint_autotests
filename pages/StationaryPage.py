from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from selenium.webdriver import Chrome


class StationaryPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        self.popular_products = '//div[contains(., "Популярное") ' \
                                'and contains(@class, "section-name")]/../..' \
                                '//div[contains(@class, "product need-watch")]'
        self.first_popular_product = f'({self.popular_products})[1]'

    def get_first_popular_product_title(self):
        return self.driver.find_element(
            By.XPATH,
            self.first_popular_product +
            "//span[contains(@class, 'product-title')]"
        ).text

    def click_by_cart_for_first_popular_product(self):
        return self.driver.find_element(
            By.XPATH,
            self.first_popular_product +
            "//a[contains(@class, 'buy-link')]"
        ).click()
