from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskCreatePage:
    title_input = (By.NAME, "title")

    assignee_combobox = (
        By.XPATH,
        "//div[contains(@class, 'MuiFormControl-root')"
        "][.//label[contains(., 'Assignee')]]//*[@role='combobox']"
    )

    status_combobox = (
        By.XPATH,
        "//div[contains(@class, 'MuiFormControl-root')"
        "][.//label[contains(., 'Status')]]//*[@role='combobox']"
    )

    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    created_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element created')]"
    )

    def __init__(self, browser):
        self.browser = browser

    def title_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.title_input)
        ).is_displayed()

    def assignee_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.assignee_combobox)
        ).is_displayed()

    def status_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.status_combobox)
        ).is_displayed()

    def fill_title(self, title):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.title_input)
        ).send_keys(title)

    def select_first_option(self, locator):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        ).click()

        first_option = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[role="option"]')
            )
        )

        option_text = first_option.text.strip()
        option_value = first_option.get_attribute("data-value")

        first_option.click()

        return option_text, option_value

    def select_first_assignee(self):
        return self.select_first_option(self.assignee_combobox)

    def select_first_status(self):
        return self.select_first_option(self.status_combobox)

    def save_task(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def creation_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.created_notification
            )
        ).is_displayed()

    def select_status_by_name(self, status_name):
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