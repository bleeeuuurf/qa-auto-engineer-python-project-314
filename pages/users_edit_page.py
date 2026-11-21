from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class UsersEditPage(BasePage):
    email_input = (By.NAME, "email")
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')
    email_error = (By.XPATH, "//p[normalize-space()='Incorrect email format']")

    def clear_field(self, locator):
        field = self.find_visible_element(locator)

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)

        self.wait_for_field_to_be_empty(field)

    def save_user(self):
        self.click_element(self.save_button)

    def get_email(self):
        return self.find_visible_element(self.email_input).get_attribute("value")

    def get_first_name(self):
        return self.find_visible_element(self.first_name_input).get_attribute("value")

    def get_last_name(self):
        return self.find_visible_element(self.last_name_input).get_attribute("value")

    def update_user(self, email, first_name, last_name):
        self.update_email(email)

        self.clear_field(self.first_name_input)
        self.enter_text(self.first_name_input, first_name)

        self.clear_field(self.last_name_input)
        self.enter_text(self.last_name_input, last_name)

    def email_is_invalid(self):
        return self.wait_for_attribute(self.email_input, "aria-invalid", "true")

    def email_error_is_displayed(self):
        return self.is_element_visible(self.email_error)

    def update_email(self, email):
        self.clear_field(self.email_input)
        self.enter_text(self.email_input, email)
