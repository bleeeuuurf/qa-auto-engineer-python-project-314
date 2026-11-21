
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class UsersPage(BasePage):
    users_menu_item = (By.CSS_SELECTOR, 'a[href="#/users"]')

    page_title = (By.ID, "react-admin-title")
    users_table = (By.CSS_SELECTOR, "table")
    email_column = (By.CSS_SELECTOR, "th.column-email")
    first_name_column = (By.CSS_SELECTOR, "th.column-firstName")
    last_name_column = (By.CSS_SELECTOR, "th.column-lastName")

    create_button = (By.CSS_SELECTOR, 'a[href="#/users/create"]')
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')

    select_all_checkbox = (
        By.XPATH,
        "//input[@aria-label='Select all']"
        "/ancestor::span[contains(@class, 'MuiCheckbox-root')]"
    )

    empty_list_message = (
        By.XPATH,
        "//p[normalize-space()='No Users yet.']"
    )

    def open_page(self):
        self.click_element(self.users_menu_item)

    def page_is_opened(self):
        return self.get_element_text(self.page_title) == "Users"

    def table_is_loaded(self):
        self.find_visible_element(self.users_table)

        return all(
            self.is_element_visible(locator)
            for locator in [
                self.email_column,
                self.first_name_column,
                self.last_name_column,
            ]
        )

    def open_create_form(self):
        self.click_element(self.create_button)

    def user_is_in_table(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )

        return self.is_element_visible(user_row)

    def open_edit_form(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )

        self.click_element(user_row)

    def select_user(self, email):
        checkbox = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
            "//span[@aria-label='Select this row']"
        )

        self.click_element(checkbox)

    def delete_selected_user(self):
        self.click_element(self.delete_button)

    def deletion_notification_is_displayed(self, message):
        notification = (
            By.XPATH,
            f"//*[@role='alert' and contains(., '{message}')]"
        )

        return self.is_element_visible(notification)

    def user_is_not_in_table(self, email):
        user_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{email}']]"
        )

        return self.wait_until_invisible(user_row)

    def select_all_users(self):
        self.click_element(self.select_all_checkbox)

    def users_list_is_empty(self):
        return self.is_element_visible(self.empty_list_message)
