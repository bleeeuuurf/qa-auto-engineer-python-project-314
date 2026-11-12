
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    sign_in_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_page(self):
        self.browser.get(self.base_url)

    def login(self, username, password):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.sign_in_button).click()

