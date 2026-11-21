from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class TaskStatusEditPage(BasePage):
    name_input = (By.NAME, "name")
    slug_input = (By.NAME, "slug")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    def name_is_displayed(self):
        return self.is_element_visible(self.name_input)

    def slug_is_displayed(self):
        return self.is_element_visible(self.slug_input)

    def update_field(self, locator, value):
        field = self.find_visible_element(locator)

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)
        self.wait_for_field_to_be_empty(field)
        field.send_keys(value)

    def update_status(self, name, slug):
        self.update_field(self.name_input, name)
        self.update_field(self.slug_input, slug)

    def save_status(self):
        self.click_element(self.save_button)
