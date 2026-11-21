
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class LabelEditPage(BasePage):
    name_input = (By.NAME, "name")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    updated_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element updated')]"
    )

    def name_is_displayed(self):
        return self.is_element_visible(self.name_input)

    def clear_field(self, locator):
        field = self.find_visible_element(locator)

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)

        self.wait_for_field_to_be_empty(field)

    def update_label_name(self, new_name):
        self.clear_field(self.name_input)
        self.enter_text(self.name_input, new_name)

    def save_label(self):
        self.click_element(self.save_button)

    def update_notification_is_displayed(self):
        return self.is_element_visible(self.updated_notification)
