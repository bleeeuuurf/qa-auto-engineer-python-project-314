import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
def test_login_page_smoke(browser, base_url):
    browser.get(base_url)

    assert browser.title == "Task manager"

    username = browser.find_element(By.NAME, "username")

    password = browser.find_element(By.NAME, "password")
    sign_in_button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )

    assert username.is_displayed()
    assert password.is_displayed()
    assert sign_in_button.is_displayed()
    assert sign_in_button.text == "SIGN IN"
