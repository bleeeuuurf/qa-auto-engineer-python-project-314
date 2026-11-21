
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskEditPage:
    title_input = (By.NAME, "title")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    updated_notification = (By.XPATH,"//*[@role='alert' and contains(., 'Element updated')]")
    status_combobox = (By.XPATH,"//div[contains(@class, 'MuiFormControl-root')][.//label[contains(., 'Status')]]//*[@role='combobox']")

    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    deleted_notification = (By.XPATH,"//*[@role='alert' and contains(., 'deleted')]")

    def __init__(self, browser):
        self.browser = browser

    def title_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.title_input)
        ).is_displayed()

    def get_title(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.title_input)
        ).get_attribute("value")

    def clear_field(self, locator):
        field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator)
        )

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)

        WebDriverWait(self.browser, 5).until(
            lambda browser: field.get_attribute("value") == ""
        )

    def update_title(self, new_title):
        self.clear_field(self.title_input)

        field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.title_input)
        )
        field.send_keys(new_title)

    def save_task(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def update_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.updated_notification
            )
        ).is_displayed()

    def select_status(self, status_name):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.status_combobox)
        ).click()

        option_locator = (
            By.XPATH,
            f"//li[@role='option' "
            f"and normalize-space()='{status_name}']"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(option_locator)
        ).click()

    def select_filter_option_by_name(self, filter_locator, option_name):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(filter_locator)
        ).click()

        option_locator = (
            By.XPATH,
            f"//li[@role='option' "
            f"and normalize-space()='{option_name}']"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(option_locator)
        ).click()

    def filter_by_status(self, status_name):
        self.select_filter_option_by_name(
            self.status_filter,
            status_name
        )

    def delete_task(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()

    def deletion_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.deleted_notification
            )
        ).is_displayed()