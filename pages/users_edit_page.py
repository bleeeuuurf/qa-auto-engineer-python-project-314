from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class UsersEditPage:
    email_input = (By.NAME, "email")
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')
    email_error = (By.XPATH,"//p[normalize-space()='Incorrect email format']")

    def __init__(self, browser):
        self.browser = browser

    def enter_text(self, locator, value):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(value)

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
        
    def save_user(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()    

    def get_email(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.email_input)
        ).get_attribute("value")

    def get_first_name(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).get_attribute("value")

    def get_last_name(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).get_attribute("value")

    def update_user(self, email, first_name, last_name):
        self.update_email(email)

        self.clear_field(self.first_name_input)
        self.browser.find_element(*self.first_name_input).send_keys(first_name)

        self.clear_field(self.last_name_input)
        self.browser.find_element(*self.last_name_input).send_keys(last_name)

    def email_is_invalid(self):
        return WebDriverWait(self.browser, 5).until(
            lambda browser: browser.find_element(
                *self.email_input
            ).get_attribute("aria-invalid") == "true"
        )

    def email_error_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.email_error)
        ).is_displayed()

    def update_email(self, email):
        email_field = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.email_input)
        )

        email_field.click()
        email_field.send_keys(Keys.HOME)
        email_field.send_keys(Keys.SHIFT, Keys.END)
        email_field.send_keys(Keys.BACKSPACE)

        WebDriverWait(self.browser, 5).until(
            lambda browser: email_field.get_attribute("value") == ""
        )

        email_field.send_keys(email)