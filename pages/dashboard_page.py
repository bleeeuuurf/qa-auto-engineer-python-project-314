
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    profile_button = (By.CSS_SELECTOR, "button[aria-label='Profile']")
    logout_button = (By.XPATH, "//li[@role='menuitem' and .//span[text()='Logout']]")
    page_title = (By.ID, "react-admin-title")

    def __init__(self, browser):
        self.browser = browser

    def page_is_opened(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.page_title)
        ).text == "Welcome to the administration"

    def logout(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.profile_button)
        ).click()

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

