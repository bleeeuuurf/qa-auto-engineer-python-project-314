from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabelCreatePage:
    name_input = (By.NAME, "name")
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

    def fill_label_form(self, name):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)

    def save_label(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def creation_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.created_notification
            )
        ).is_displayed()