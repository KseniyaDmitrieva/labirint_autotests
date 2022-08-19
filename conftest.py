import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path


@pytest.fixture(autouse=True, scope="class")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("log-level=3")
    chrome_options.add_argument("--window-size=1920x1080")
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object, options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.close()
