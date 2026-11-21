from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LabelsPage(BasePage):
    labels_menu_item = (By.CSS_SELECTOR, 'a[href="#/labels"]')
    create_button = (By.CSS_SELECTOR, 'a[href="#/labels/create"]')
    labels_table = (By.CSS_SELECTOR, "table")
    name_cells = (By.CSS_SELECTOR, "td.column-name")
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    deleted_notification = (By.XPATH, "//*[@role='alert' and contains(., 'deleted')]")

    def open_page(self):
        self.click_element(self.labels_menu_item)

    def table_is_loaded(self):
        return self.is_element_visible(self.labels_table)

    def open_create_form(self):
        self.click_element(self.create_button)

    def label_is_in_table(self, name):
        label_row = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
            ),
        )
        return self.is_element_visible(label_row)

    def names_are_displayed(self):
        cells = self.find_visible_elements(self.name_cells)
        return all(cell.text.strip() for cell in cells)

    def open_edit_form(self, name):
        label_row = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
            ),
        )
        self.click_element(label_row)

    def select_label(self, name):
        label_checkbox = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
                "//input[@type='checkbox']"
                "/ancestor::span[contains(@class, 'MuiCheckbox-root')]"
            ),
        )
        self.click_element(label_checkbox)

    def select_labels(self, names):
        for name in names:
            self.select_label(name)

    def delete_selected_labels(self):
        self.click_element(self.delete_button)

    def deletion_notification_is_displayed(self):
        return self.is_element_visible(self.deleted_notification)

    def label_is_not_in_table(self, name):
        label_row = (
            By.XPATH,
            (
                f"//tr[.//td[contains(@class, 'column-name') "
                f"and normalize-space()='{name}']]"
            ),
        )
        return self.wait_until_invisible(label_row)
