import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


@pytest.fixture
def browser():
    options = Options()

    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("APP_BASE_URL", "http://localhost:5173").rstrip("/")


USERNAME = "test_username_without_error_0303003"
PASSWORD = "test_username_without_error_0303003"


@pytest.fixture
def logged_in_user(browser, base_url):
    login_page = LoginPage(browser, base_url)

    login_page.open_page()
    login_page.login(USERNAME, PASSWORD)

    return browser
