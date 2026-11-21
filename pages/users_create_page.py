
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UserCreatePage(BasePage):
    page_title = (By.XPATH, "//*[text()='Create User']")

    email_input = (By.NAME, "email")
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    def page_is_opened(self):
        return self.is_element_visible(self.page_title)

    def email_is_displayed(self):
        return self.is_element_visible(self.email_input)

    def first_name_is_displayed(self):
        return self.is_element_visible(self.first_name_input)

    def last_name_is_displayed(self):
        return self.is_element_visible(self.last_name_input)

    def fill_user_form(self, email, first_name, last_name):
        self.enter_text(self.email_input, email)
        self.enter_text(self.first_name_input, first_name)
        self.enter_text(self.last_name_input, last_name)

    def save_user(self):
        self.click_element(self.save_button)

