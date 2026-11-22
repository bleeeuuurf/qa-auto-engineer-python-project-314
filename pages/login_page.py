from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    sign_in_button = (By.CSS_SELECTOR, "button[type='submit']")
    users_menu_item = (By.CSS_SELECTOR, 'a[href="#/users"]')
    notification = (By.CSS_SELECTOR, ".MuiSnackbarContent-message")

    def open_page(self):
        self.open_url(self.base_url)

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.wait_until_invisible(self.notification)
        self.click_element(self.sign_in_button)
        self.find_visible_element(self.users_menu_item)

    def username_is_displayed(self):
        return self.is_element_visible(self.username_input)

    def password_is_displayed(self):
        return self.is_element_visible(self.password_input)

    def sign_in_button_is_displayed(self):
        return self.is_element_visible(self.sign_in_button)

    def sign_in_button_text(self):
        return self.get_element_text(self.sign_in_button)

    def page_title(self):
        return self.browser.title
