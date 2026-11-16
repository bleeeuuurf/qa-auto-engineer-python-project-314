from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LabelsPage:
    labels_menu_item = (By.CSS_SELECTOR, 'a[href="#/labels"]')
    create_button = (By.CSS_SELECTOR, 'a[href="#/labels/create"]')
    labels_table = (By.CSS_SELECTOR, "table")
    name_cells = (By.CSS_SELECTOR, "td.column-name")
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    deleted_notification = (By.XPATH,"//*[@role='alert' and contains(., 'deleted')]")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_page(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.labels_menu_item)
        ).click()

    def table_is_loaded(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.labels_table)
        ).is_displayed()

    def open_create_form(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def label_is_in_table(self, name):
        label_row = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(label_row)
        ).is_displayed()

    def names_are_displayed(self):
        cells = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.name_cells)
        )

        return all(cell.text.strip() for cell in cells)

    def open_edit_form(self, name):
        label_row = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(label_row)
        ).click()

    def select_label(self, name):
        label_checkbox = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
            "//input[@type='checkbox']"
            "/ancestor::span[contains(@class, 'MuiCheckbox-root')]"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(label_checkbox)
        ).click()


    def select_labels(self, names):
        for name in names:
            self.select_label(name)


    def delete_selected_labels(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()


    def deletion_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.deleted_notification
            )
        ).is_displayed()


    def label_is_not_in_table(self, name):
        label_row = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(label_row)
        )