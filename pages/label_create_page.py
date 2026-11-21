
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LabelCreatePage(BasePage):
    name_input = (By.NAME, "name")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    created_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element created')]"
    )

    def name_is_displayed(self):
        return self.is_element_visible(self.name_input)

    def fill_label_form(self, name):
        self.enter_text(self.name_input, name)

    def save_label(self):
        self.click_element(self.save_button)

    def creation_notification_is_displayed(self):
        return self.is_element_visible(self.created_notification)
