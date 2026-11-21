from conftest import PASSWORD, USERNAME

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_success_login(browser, base_url):
    login_page = LoginPage(browser, base_url)
    dashboard_page = DashboardPage(browser)

    login_page.open_page()
    login_page.login(USERNAME, PASSWORD)

    assert dashboard_page.page_is_opened()


def test_success_logout(logged_in_user):
    dashboard_page = DashboardPage(logged_in_user)
    login_page = LoginPage(logged_in_user)

    dashboard_page.logout()

    assert login_page.username_is_displayed()
    assert login_page.password_is_displayed()
