from pages.BasePage import BasePage
from pages.CartPage import CartPage
from pages.IndexPage import IndexPage
from pages.StationaryPage import StationaryPage


def test_add_product_in_cart_from_index_page(driver):
    driver.get("https://www.labirint.ru/")
    base_page = BasePage(driver)
    base_page.click_by_stationary_nav_link()
    stationary_page = StationaryPage(driver)
    title = stationary_page.get_first_popular_product_title()
    stationary_page.click_by_cart_for_first_popular_product()
    stationary_page.click_by_cart_button()
    cart_page = CartPage(driver)
    cart_page.check_title_in_cart(title)


def test_add_product_in_cart_from_product_page(driver):
    driver.get("https://www.labirint.ru/")
    index_page = IndexPage(driver)
    title, cart_button_book = index_page.get_title_and_button_for_new_book()
    cart_button_book.click()
    index_page.click_by_cart_button()
    cart_page = CartPage(driver)
    cart_page.check_title_in_cart(title)


def test_change_count_products_in_cart(driver):
    driver.get("https://www.labirint.ru/")
    index_page = IndexPage(driver)
    title, cart_button_book = index_page.get_title_and_button_for_new_book()
    cart_button_book.click()
    index_page.click_by_cart_button()
    cart_page = CartPage(driver)
    cart_page.check_count_products(1)
    cart_page.click_by_plus_first_product()
    cart_page.check_count_products(2)
    cart_page.click_by_lessen_first_product()
    cart_page.check_count_products(1)


def test_change_price_products_in_cart(driver):
    driver.get("https://www.labirint.ru/")
    index_page = IndexPage(driver)
    title, cart_button_book = index_page.get_title_and_button_for_new_book()
    price = index_page.get_price_first_book()
    cart_button_book.click()
    index_page.click_by_cart_button()
    cart_page = CartPage(driver)
    cart_page.check_price_products(price)
    cart_page.click_by_plus_first_product()
    cart_page.check_price_products(price * 2)
    cart_page.click_by_lessen_first_product()
    cart_page.check_price_products(price)


def test_add_some_products_in_cart(driver):
    driver.get("https://www.labirint.ru/")
    index_page = IndexPage(driver)
    title1, cart_button_book1 = index_page.get_title_and_button_for_new_book()
    title2, cart_button_book2 = index_page.get_title_and_button_for_new_book(2)
    index_page.click_by_add_cart_button(cart_button_book1, 1)
    index_page.click_by_add_cart_button(cart_button_book2, 2)
    index_page.click_by_cart_button()
    cart_page = CartPage(driver)
    cart_page.check_title_in_cart(title1)
    cart_page.check_title_in_cart(title2)
    assert 2 == len(cart_page.get_products())
