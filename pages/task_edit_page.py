from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class TaskEditPage(BasePage):
    title_input = (By.NAME, "title")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    updated_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element updated')]",
    )

    status_combobox = (
        By.XPATH,
        (
            "//div[contains(@class, 'MuiFormControl-root')]"
            "[.//label[contains(., 'Status')]]//*[@role='combobox']"
        ),
    )

    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')

    deleted_notification = (By.XPATH, "//*[@role='alert' and contains(., 'deleted')]")

    def title_is_displayed(self):
        return self.is_element_visible(self.title_input)

    def get_title(self):
        return self.find_visible_element(self.title_input).get_attribute("value")

    def clear_field(self, locator):
        field = self.find_visible_element(locator)

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)

        self.wait_for_field_to_be_empty(field)

    def update_title(self, new_title):
        self.clear_field(self.title_input)
        self.enter_text(self.title_input, new_title)

    def save_task(self):
        self.click_element(self.save_button)

    def update_notification_is_displayed(self):
        return self.is_element_visible(self.updated_notification)

    def select_status(self, status_name):
        self.click_element(self.status_combobox)

        option_locator = (
            By.XPATH,
            (f"//li[@role='option' and normalize-space()='{status_name}']"),
        )

        self.click_element(option_locator)

    def delete_task(self):
        self.click_element(self.delete_button)

    def deletion_notification_is_displayed(self):
        return self.is_element_visible(self.deleted_notification)
