from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabelEditPage:
    name_input = (By.NAME, "name")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    updated_notification = (
        By.XPATH,
        "//*[@role='alert' and contains(., 'Element updated')]"
    )

    def __init__(self, browser):
        self.browser = browser

    def name_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.name_input)
        ).is_displayed()

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


    def update_label_name(self, new_name):
        self.clear_field(self.name_input)

        field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.name_input)
        )
        field.send_keys(new_name)

    def save_label(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    def update_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.updated_notification
            )
        ).is_displayed()