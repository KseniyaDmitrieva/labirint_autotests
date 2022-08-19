from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from selenium.webdriver import Chrome


class IndexPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        self.new_kids_books = '//a[contains(., ' \
                              '"Новая детская литература")]/../..' \
                              '//div[contains(@class, ' \
                              '"product need-watch")]'

    def get_new_kids_books(self):
        return self.driver.find_elements(By.XPATH, self.new_kids_books)

    def get_title_and_button_for_new_book(self, number=1):
        common_part_selector = f'({self.new_kids_books})[{number}]'
        title_element = common_part_selector + '//span[contains' \
                                               '(@class, "product-title")]'
        cart_button_element = common_part_selector + '//a[contains' \
                                                     '(@class, "buy-link")]'

        title = self.driver.find_element(By.XPATH, title_element).text
        cart_button = self.driver.find_element(By.XPATH, cart_button_element)
        return title, cart_button

    def get_price_first_book(self):
        price_element = self.new_kids_books + '//span[contains(' \
                                              '@class, "price-val")]' \
                                              '/span'
        price = int(self.driver.find_elements(
            By.XPATH,
            price_element
        )[0].text.replace(" ", ""))
        return price

    def click_by_add_cart_button(self, button: WebElement, number_of_product):
        button.click()
        common_part_selector = f'({self.new_kids_books})[{number_of_product}]'
        cart_button_element = common_part_selector + '//a[contains(' \
                                                     '@class, "buy-link") ' \
                                                     'and contains(., ' \
                                                     '"ОФОРМИТЬ")]'
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, cart_button_element)))
