import pytest

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from conftest import USERNAME, PASSWORD


@pytest.mark.smoke
def test_success_login(browser, base_url):
    login_page = LoginPage(browser, base_url)
    dashboard_page = DashboardPage(browser)

    login_page.open_page()
    login_page.login(USERNAME, PASSWORD)

    assert dashboard_page.page_is_opened()


@pytest.mark.smoke
def test_success_logout(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)

    dashboard_page.logout()

    assert logged_in_user.find_element(By.NAME, "username").is_displayed()
    assert logged_in_user.find_element(By.NAME, "password").is_displayed()