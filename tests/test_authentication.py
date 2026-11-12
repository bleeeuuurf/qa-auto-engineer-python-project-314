import pytest

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
def test_success_login(browser, base_url):
    login_page = LoginPage(browser, base_url)
    dashboard_page = DashboardPage(browser)

    login_page.open_page()
    login_page.login("test", "test")

    assert dashboard_page.page_is_opened()

@pytest.mark.smoke
def test_success_logout(browser, base_url):
    login_page = LoginPage(browser, base_url)
    dashboard_page = DashboardPage(browser)

    login_page.open_page()
    login_page.login("test", "test")

    assert dashboard_page.page_is_opened()

    dashboard_page.logout()

    assert browser.find_element(By.NAME, "username").is_displayed()
    assert browser.find_element(By.NAME, "password").is_displayed()
