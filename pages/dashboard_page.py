
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    profile_button = (By.CSS_SELECTOR, "button[aria-label='Profile']")
    logout_button = (
        By.XPATH,
        "//li[@role='menuitem' and .//span[text()='Logout']]"
    )
    page_title = (By.ID, "react-admin-title")

    def page_is_opened(self):
        return self.get_element_text(self.page_title) == (
            "Welcome to the administration"
        )

    def logout(self):
        self.click_element(self.profile_button)
        self.click_element(self.logout_button)

