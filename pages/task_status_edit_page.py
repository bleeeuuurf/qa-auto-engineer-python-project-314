
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskStatusEditPage:
    name_input = (By.NAME, "name")
    slug_input = (By.NAME, "slug")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

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

    def update_field(self, locator, value):
        field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator)
        )

        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(Keys.SHIFT, Keys.END)
        field.send_keys(Keys.BACKSPACE)
        field.send_keys(value)

    def update_status(self, name, slug):
        self.update_field(self.name_input, name)
        self.update_field(self.slug_input, slug)

    def save_status(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
