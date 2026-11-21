from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TaskStatusCreatePage(BasePage):
    name_input = (By.NAME, "name")
    slug_input = (By.NAME, "slug")
    created_at_input = (By.NAME, "createdAt")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    created_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element created')]",
    )

    def name_is_displayed(self):
        return self.is_element_visible(self.name_input)

    def slug_is_displayed(self):
        return self.is_element_visible(self.slug_input)

    def created_at_is_displayed(self):
        return self.is_element_visible(self.created_at_input)

    def fill_status_form(self, name, slug):
        self.enter_text(self.name_input, name)
        self.enter_text(self.slug_input, slug)

    def save_status(self):
        self.click_element(self.save_button)

    def creation_notification_is_displayed(self):
        return self.is_element_visible(self.created_notification)
