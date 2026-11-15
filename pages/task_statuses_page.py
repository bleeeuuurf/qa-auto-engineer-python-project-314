from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaskStatusesPage:
    statuses_menu_item = (By.CSS_SELECTOR,'a[href="#/task_statuses"]')
    create_button = (By.CSS_SELECTOR,'a[href="#/task_statuses/create"]')
    statuses_table = (By.CSS_SELECTOR, "table")
    name_cells = (By.CSS_SELECTOR, "td.column-name")
    slug_cells = (By.CSS_SELECTOR, "td.column-slug")
    delete_button = (By.CSS_SELECTOR, 'button[aria-label="Delete"]')
    deleted_notification = (By.XPATH,"//*[@role='alert' and contains(., 'deleted')]")
    select_all_checkbox = (By.XPATH,"//input[@aria-label='Select all']/ancestor::span[contains(@class, 'MuiCheckbox-root')]")
    empty_list_message = (By.XPATH, "//div[contains(@class, 'RaEmpty-message')]//p[normalize-space()='No Task statuses yet.']")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_page(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.statuses_menu_item)
        ).click()

    def table_is_loaded(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.statuses_table)
        ).is_displayed()

    def open_create_form(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def status_is_in_table(self, name, slug):
        status_row = (
            By.XPATH,
            f"//tr[.//*[normalize-space()='{name}']"
            f" and .//*[normalize-space()='{slug}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(status_row)
        ).is_displayed()

    def names_are_displayed(self):
        cells = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.name_cells)
        )
        return all(cell.text.strip() for cell in cells)

    def slugs_are_displayed(self):
        cells = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.slug_cells)
        )
        return all(cell.text.strip() for cell in cells)

    def open_edit_form(self, name):
        status_row = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(status_row)
        ).click()

    def select_status(self, name):
        status_checkbox = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
            f"//span[@aria-label='Select this row']"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(status_checkbox)
        ).click()


    def delete_selected_statuses(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()


    def deletion_notification_is_displayed(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.deleted_notification
            )
        ).is_displayed()

    def status_is_not_in_table(self, name):
        status_row = (
            By.XPATH,
            f"//tr[.//td[contains(@class, 'column-name') "
            f"and normalize-space()='{name}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(status_row)
        )

    def select_all_statuses(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.select_all_checkbox)
        ).click()


    def statuses_list_is_empty(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(
                self.empty_list_message
            )
        ).is_displayed()