from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from selenium.webdriver import Chrome


class CartPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        self.products = '//div[contains(@class, "product-cart")]'
        self.count_products = ''

    def get_products(self):
        return self.driver.find_elements(By.XPATH, self.products)

    def check_count_products(self, number):
        assert self.driver.find_element(
            By.XPATH,
            f'//span[@id = "basket-default-prod-count2" '
            f'and contains(., "{number} товар")]'
        ).is_displayed()

    def click_by_plus_first_product(self):
        self.driver.find_element(
            By.XPATH,
            f'({self.products})[1]'
            f'//span[contains(@class, "btn-increase-cart")]'
        ).click()

    def click_by_lessen_first_product(self):
        self.driver.find_element(
            By.XPATH,
            f'({self.products})[1]//span[contains(@class, "btn-lessen-cart")]'
        ).click()

    def check_price_products(self, number):
        number = '{0:,}'.format(number).replace(',', ' ')
        assert self.driver.find_element(
            By.XPATH,
            f'//span[@id="basket-default-sumprice-discount" '
            f'and contains(., "{number}")]'
        )

    def check_title_in_cart(self, title):
        products = self.driver.find_elements(
                By.XPATH,
                "//span[contains(@class, 'product-title')]"
            )
        products_title = []
        for product in products:
            title_book = product.text
            products_title.append(title_book)
        assert title in products_title
