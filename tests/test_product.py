import pytest

from pages.ProductPage import ProductPage


product_urls = [
    "https://www.labirint.ru/books/838684/",
    "https://www.labirint.ru/games/552689/",
    "https://www.labirint.ru/office/814599/",
    "https://www.labirint.ru/multimedia/247550/",
    "https://www.labirint.ru/souvenir/851515/",
    "https://www.labirint.ru/household/745243/",
]

product_info = [
    (
        "https://www.labirint.ru/games/552689/",
        "552689",
        "4607091409041",
        "2 г",
        "80x113x1 мм"
    ),
    (
        "https://www.labirint.ru/books/838684/",
        "838684",
        "978-5-907500-01-3",
        "658 г",
        "217x150x28 мм"
        ""),
    (
        "https://www.labirint.ru/office/814599/",
        "814599",
        "4630074955256",
        "8 г",
        "160x60x3 мм"
    ),
    (
        "https://www.labirint.ru/multimedia/247550/",
        "247550",
        "4607031761434",
        "80 г",
        "125x143x9 мм"
    ),
    (
        "https://www.labirint.ru/souvenir/851515/",
        "851515",
        "4607811853748",
        "10 г",
        "285x205x1 мм"
    ),
    (
        "https://www.labirint.ru/household/745243/",
        "745243",
        "4606224142043",
        "36 г",
        "170x90x50 мм"
    ),
]


@pytest.mark.parametrize('url', product_urls)
def test_header_fixed(driver, url):
    driver.get(url)
    product_page = ProductPage(driver)
    product_page.scroll(500)
    product_page.see_element_header_fixed()


@pytest.mark.parametrize('url,product_id,isbn,weight,size', product_info)
def test_info(driver, url, product_id, isbn, weight, size):
    driver.get(url)
    product_page = ProductPage(driver)
    assert product_id in product_page.get_text_from_element(product_page.id)
    assert isbn in product_page.get_text_from_element(product_page.isbn)
    assert weight in product_page.get_text_from_element(product_page.weight)
    assert size in product_page.get_text_from_element(product_page.size)


@pytest.mark.parametrize('url', product_urls)
def test_login_modal_after_click_by_write_review(driver, url):
    driver.get(url)
    product_page = ProductPage(driver)
    product_page.click_by_cookie_policy_button()
    product_page.click_by_write_review_button()
    product_page.see_auth_header()


@pytest.mark.parametrize('url', product_urls)
def test_login_modal_after_click_by_star(driver, url):
    driver.get(url)
    product_page = ProductPage(driver)
    product_page.click_by_star()
    product_page.see_auth_header()


@pytest.mark.parametrize('url', product_urls)
def test_login_modal_after_click_by_fave_button(driver, url):
    driver.get(url)
    product_page = ProductPage(driver)
    product_page.click_by_add_to_fave_button()
    product_page.see_popup_add_in_fave()


@pytest.mark.parametrize('url', product_urls)
def test_count_popular_products(driver, url):
    driver.get(url)
    product_page = ProductPage(driver)
    assert 6 == product_page.get_count_popular_products()
