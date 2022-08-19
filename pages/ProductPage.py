from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        self.element_header_fixed = '//div[contains(@class, ' \
                                    '"header-fixed")]' \
                                    '/div[contains(@class, "relative")]'
        self.id = '.articul'
        self.isbn = '.isbn'
        self.weight = '.weight'
        self.size = '.dimensions'
        self.write_review_button = '//div[contains(@class, ' \
                                   '"write-comment__buttons")]/a'
        self.auth_header = '//div[contains(@class, "auth-header")]'
        self.stars = '//span[@id="product-rating-stars"]/span'
        self.add_in_fave = '//a[contains(@class, "fave")]' \
                           '/span[contains(., "отложенные")]'
        self.popup_add_in_fave = '//div[contains(@class, ' \
                                 '"popup-window-content")]' \
                                 '//div[contains(., ' \
                                 '"Вы добавили  в отложенные товар")]'
        self.popular_product = '//div[contains(@class, "products-row") ' \
                               'and contains(@data-title, "Популярные")]' \
                               '/div[contains(@class, "product")]'

    def see_element_header_fixed(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.element_header_fixed)
            )
        )

    def get_text_from_element(self, element):
        return self.driver.find_element(By.CSS_SELECTOR, element).text

    def click_by_write_review_button(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.write_review_button)
        action.scroll_to_element(element)
        element.click()

    def see_auth_header(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.auth_header))
        )

    def click_by_star(self, number=10):
        self.driver.find_element(By.XPATH, f'({self.stars})[{number}]').click()

    def click_by_add_to_fave_button(self):
        self.driver.find_element(By.XPATH, self.add_in_fave).click()

    def see_popup_add_in_fave(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.add_in_fave))
        )

    def get_count_popular_products(self):
        return len(self.driver.find_elements(By.XPATH, self.popular_product))
