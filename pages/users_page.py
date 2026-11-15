
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UsersPage:
    users_menu_item = (By.CSS_SELECTOR, 'a[href="#/users"]')

    page_title = (By.ID, "react-admin-title")
    users_table = (By.CSS_SELECTOR, "table")
    email_column = (By.CSS_SELECTOR, "th.column-email")
    first_name_column = (By.CSS_SELECTOR, "th.column-firstName")
    last_name_column = (By.CSS_SELECTOR, "th.column-lastName")
    create_button = (By.CSS_SELECTOR, 'a[href="#/users/create"]')
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    delete_notification = (By.XPATH,"//*[@role='alert' and contains(., 'Element deleted')]")
    select_all_checkbox = (By.XPATH, "//input[@aria-label='Select all']/ancestor::span[contains(@class, 'MuiCheckbox-root')]")
    empty_list_message = (By.XPATH, "//p[normalize-space()='No Users yet.']")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_page(self):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.users_menu_item)
        ).click()

    def page_is_opened(self):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.page_title)
        ).text == "Users"

    def table_is_loaded(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.users_table)
        )

        return all(
            self.browser.find_element(*locator).is_displayed()
            for locator in [
                self.email_column,
                self.first_name_column,
                self.last_name_column,
            ]
        )

    def open_create_form(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def user_is_in_table(self, email):
        user_row = (By.XPATH,f"//tr[.//*[normalize-space()='{email}']]")

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(user_row)
        ).is_displayed()

    def open_edit_form(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(user_row)
        ).click()

    def select_user(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )
        checkbox = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
            "//span[@aria-label='Select this row']"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(checkbox)
        ).click()

    def delete_selected_user(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()

    def deletion_notification_is_displayed(self, message):
        notification = (
            By.XPATH,
            f"//*[@role='alert' and contains(., '{message}')]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(notification)
        ).is_displayed()

    def user_is_not_in_table(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(user_row)
        )
    def select_all_users(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.select_all_checkbox)
        ).click()

    def users_list_is_empty(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.empty_list_message
            )
        ).is_displayed()