from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskStatusCreatePage:
    name_input = (By.NAME, "name")
    slug_input = (By.NAME, "slug")
    created_at_input = (By.NAME, "createdAt")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    created_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element created')]"
    )

    def __init__(self, browser):
        self.browser = browser

    def name_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.name_input)
        ).is_displayed()

    def slug_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.slug_input)
        ).is_displayed()

    def created_at_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.created_at_input)
        ).is_displayed()

    def fill_status_form(self, name, slug):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)

        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.slug_input)
        ).send_keys(slug)

    def save_status(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def creation_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.created_notification
            )
        ).is_displayed()