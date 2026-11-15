
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserCreatePage:
    page_title = (By.XPATH, "//*[text()='Create User']")

    email_input = (By.NAME, "email")
    first_name_input = (By.NAME, "firstName")
    last_name_input = (By.NAME, "lastName")
    save_button = (By.CSS_SELECTOR, 'button[aria-label="Save"]')

    def __init__(self, browser):
        self.browser = browser

    def page_is_opened(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.page_title)
        ).is_displayed()

    def email_is_displayed(self):
        return self.browser.find_element(*self.email_input).is_displayed()

    def first_name_is_displayed(self):
        return self.browser.find_element(*self.first_name_input).is_displayed()

    def last_name_is_displayed(self):
        return self.browser.find_element(*self.last_name_input).is_displayed()

    def fill_user_form(self, email, first_name, last_name):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.email_input)
        ).send_keys(email)

        self.browser.find_element(*self.first_name_input).send_keys(first_name)
        self.browser.find_element(*self.last_name_input).send_keys(last_name)

    def save_user(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()    
    
