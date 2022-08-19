import pytest

from pages.BasePage import BasePage
from pages.SearchResultPage import SearchResultPage

titles = [
    ("https://www.labirint.ru/", "Лабиринт"),
    ("https://www.labirint.ru/books/870765/", "Миндаль"),
]


different_pages = [
    "https://www.labirint.ru/",
    "https://www.labirint.ru/books/870765/",
    "https://www.labirint.ru/cart/",
]

search_texts = [
    ("Стивен Кинг", 686),
    ("Тетрадь", 23930),
    ("Atljh Ljcnjtdcrbq", 771)
]


@pytest.mark.parametrize("url, title", titles)
def test_titles(driver, url, title):
    driver.get(url)
    assert title in driver.title


@pytest.mark.parametrize("url", different_pages)
def test_logo_click(driver, url):
    driver.get(url)
    base_page = BasePage(driver)
    base_page.click_by_logo()
    assert "Книжный интернет-магазин" in driver.title


@pytest.mark.parametrize("text, count_results", search_texts)
def test_search_results(driver, text, count_results):
    driver.get("https://www.labirint.ru/")
    base_page = BasePage(driver)
    base_page.fill_search_field(text)
    base_page.click_by_search_button()
    search_result = SearchResultPage(driver)
    assert count_results == search_result.get_total_results()


def test_search_results_with_unknown_request(driver):
    driver.get("https://www.labirint.ru/")
    base_page = BasePage(driver)
    base_page.fill_search_field("Розетка ЛК-364")
    base_page.click_by_search_button()
    search_result = SearchResultPage(driver)
    assert "Мы ничего не нашли по вашему запросу! Что делать?" \
           in search_result.get_text_from_empty_result()


@pytest.mark.parametrize("url", different_pages)
def test_accept_cookie(driver, url):
    driver.get(url)
    base_page = BasePage(driver)
    base_page.see_cookie_policy()
    base_page.click_by_cookie_policy_button()
    base_page.not_see_cookie_policy()
