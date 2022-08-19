from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from selenium.webdriver import Chrome


class SearchResultPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)

        self.total_results = '//span[contains(.,"Товары")]/' \
                             '..//span[contains(@class, "search-tab-count")]'
        self.empty_result = '//div[contains(@class,"search-error")]/h1'

    def get_total_results(self):
        return int(self.driver.find_element(
            By.XPATH,
            self.total_results
        ).text.replace(" ", ""))

    def get_text_from_empty_result(self):
        return self.driver.find_element(
            By.XPATH,
            self.empty_result
        ).text
