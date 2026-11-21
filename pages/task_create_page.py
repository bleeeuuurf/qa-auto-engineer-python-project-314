from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TaskCreatePage(BasePage):
    title_input = (By.NAME, "title")

    assignee_combobox = (
        By.CSS_SELECTOR,
        ".ra-input-assignee_id [role='combobox']",
    )

    status_combobox = (
        By.XPATH,
        (
            "//div[contains(@class, 'MuiFormControl-root')"
            "][.//label[contains(., 'Status')]]//*[@role='combobox']"
        ),
    )

    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    created_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element created')]",
    )

    def title_is_displayed(self):
        return self.is_element_visible(self.title_input)

    def assignee_is_displayed(self):
        return self.is_element_visible(self.assignee_combobox)

    def status_is_displayed(self):
        return self.is_element_visible(self.status_combobox)

    def fill_title(self, title):
        self.enter_text(self.title_input, title)

    def select_first_option(self, locator):
        self.click_element(locator)

        option_locator = (
            By.CSS_SELECTOR,
            'ul[role="listbox"] li[role="option"]',
        )

        first_option = self.find_visible_element(option_locator)

        option_text = first_option.text.strip()
        option_value = first_option.get_attribute("data-value")

        first_option.click()

        return option_text, option_value

    def select_first_assignee(self):
        return self.select_first_option(self.assignee_combobox)

    def select_first_status(self):
        return self.select_first_option(self.status_combobox)

    def save_task(self):
        self.click_element(self.save_button)

    def creation_notification_is_displayed(self):
        return self.is_element_visible(self.created_notification)

    def select_status_by_name(self, status_name):
        self.click_element(self.status_combobox)

        option_locator = (
            By.XPATH,
            (f"//li[@role='option' and normalize-space()='{status_name}']"),
        )

        self.click_element(option_locator)
