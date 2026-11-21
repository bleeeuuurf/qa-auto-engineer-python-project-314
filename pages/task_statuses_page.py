from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TaskStatusesPage(BasePage):
    statuses_menu_item = (By.CSS_SELECTOR, 'a[href="#/task_statuses"]')
    create_button = (By.CSS_SELECTOR, 'a[href="#/task_statuses/create"]')
    statuses_table = (By.CSS_SELECTOR, "table")
    name_cells = (By.CSS_SELECTOR, "td.column-name")
    slug_cells = (By.CSS_SELECTOR, "td.column-slug")
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    deleted_notification = (By.XPATH, "//*[@role='alert' and contains(., 'deleted')]")
    select_all_checkbox = (
        By.XPATH,
        (
            "//input[@aria-label='Select all']"
            "/ancestor::span[contains(@class, 'MuiCheckbox-root')]"
        ),
    )
    empty_list_message = (
        By.XPATH,
        (
            "//div[contains(@class, 'RaEmpty-message')]"
            "//p[normalize-space()='No Task statuses yet.']"
        ),
    )

    def open_page(self):
        self.click_element(self.statuses_menu_item)

    def table_is_loaded(self):
        return self.is_element_visible(self.statuses_table)

    def open_create_form(self):
        self.click_element(self.create_button)

    def status_is_in_table(self, name, slug):
        status_row = (
            By.XPATH,
            (
                f"//tr[.//*[normalize-space()='{name}']"
                f" and .//*[normalize-space()='{slug}']]"
            ),
        )
        return self.is_element_visible(status_row)

    def names_are_displayed(self):
        cells = self.find_visible_elements(self.name_cells)
        return all(cell.text.strip() for cell in cells)

    def slugs_are_displayed(self):
        cells = self.find_visible_elements(self.slug_cells)
        return all(cell.text.strip() for cell in cells)

    def open_edit_form(self, name):
        status_row = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
            ),
        )
        self.click_element(status_row)

    def select_status(self, name):
        status_checkbox = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
                f"//span[@aria-label='Select this row']"
            ),
        )
        self.click_element(status_checkbox)

    def delete_selected_statuses(self):
        self.click_element(self.delete_button)

    def deletion_notification_is_displayed(self):
        return self.is_element_visible(self.deleted_notification)

    def status_is_not_in_table(self, name):
        status_row = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
            ),
        )
        return self.wait_until_invisible(status_row)

    def select_all_statuses(self):
        self.click_element(self.select_all_checkbox)

    def statuses_list_is_empty(self):
        return self.is_element_visible(self.empty_list_message)
