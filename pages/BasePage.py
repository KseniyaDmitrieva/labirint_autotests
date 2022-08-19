import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver
        self.logo = '//a[contains(@class, "e-logo")]' \
                    '/span[contains(@class, "logo")]'
        self.search_field = '#search-field'
        self.search_button = '//span[contains(., "Искать") ' \
                             'and contains(@class, "b-search")]'
        self.cart_button = '//span[contains(@class, "b-header") ' \
                           'and contains(., "Корзина")]'
        self.stationary_nav_link = '//a[contains(., "Канцтовары") ' \
                                   'and contains(@class, "b-menu-e-text")]'
        self.cookie_policy_button = '.cookie-policy__button'
        self.cookie_policy_element = '.cookie-policy'

    def click_by_logo(self):
        self.driver.find_element(By.XPATH, self.logo).click()

    def fill_search_field(self, text):
        self.driver.find_element(
            By.CSS_SELECTOR,
            self.search_field
        ).send_keys(text)

    def click_by_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button).click()

    def click_by_cart_button(self):
        self.driver.find_element(By.XPATH, self.cart_button).click()

    def click_by_stationary_nav_link(self):
        self.driver.find_element(By.XPATH, self.stationary_nav_link).click()

    def click_by_cookie_policy_button(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            self.cookie_policy_button
        ).click()

    def see_cookie_policy(self):
        assert self.driver.find_element(
            By.CSS_SELECTOR,
            self.cookie_policy_element
        ).is_displayed()

    def not_see_cookie_policy(self):
        time.sleep(0.5)
        style_attributes = self.driver.find_element(
            By.CSS_SELECTOR,
            self.cookie_policy_element
        ).get_attribute('style')
        assert 'display: none' in style_attributes

    def scroll(self, number):
        self.driver.execute_script(f'window.scrollBy(0, {number})')
