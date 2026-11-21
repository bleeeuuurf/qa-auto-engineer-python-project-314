import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_page_smoke(browser, base_url):
    login_page = LoginPage(browser, base_url)

    login_page.open_page()

    assert login_page.page_title() == "Task manager"
    assert login_page.username_is_displayed()
    assert login_page.password_is_displayed()
    assert login_page.sign_in_button_is_displayed()
    assert login_page.sign_in_button_text() == "SIGN IN"
