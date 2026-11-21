
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TasksPage(BasePage):
    tasks_menu_item = (By.CSS_SELECTOR, 'a[href="#/tasks"]')
    create_button = (By.CSS_SELECTOR, 'a[href="#/tasks/create"]')

    task_columns = (By.CSS_SELECTOR, '[data-rfd-droppable-id]')

    assignee_filter = (
        By.XPATH,
        "//div[contains(@class, 'MuiFormControl-root')]"
        "[.//label[contains(., 'Assignee')]]//*[@role='combobox']"
    )

    status_filter = (
        By.XPATH,
        "//div[contains(@class, 'MuiFormControl-root')]"
        "[.//label[contains(., 'Status')]]//*[@role='combobox']"
    )

    label_filter = (
        By.XPATH,
        "//div[contains(@class, 'MuiFormControl-root')]"
        "[.//label[contains(., 'Label')]]//*[@role='combobox']"
    )

    task_cards = (
        By.CSS_SELECTOR,
        "div[data-rfd-draggable-id]"
    )

    task_titles = (
        By.CSS_SELECTOR,
        "div[data-rfd-draggable-id] .MuiTypography-h5"
    )

    edit_button = (By.CSS_SELECTOR, 'a[aria-label="Edit"]')

    def open_page(self):
        self.click_element(self.tasks_menu_item)

    def board_is_loaded(self):
        return self.find_any_visible_elements(self.task_columns)

    def open_create_form(self):
        self.click_element(self.create_button)

    def task_is_in_column(self, title, status_id):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-droppable-id='{status_id}']"
            f"//div[@data-rfd-draggable-id]"
            f"[.//*[normalize-space()='{title}']]"
        )

        return self.is_element_visible(task_card)

    def tasks_are_displayed(self):
        cards = self.find_visible_elements(self.task_cards)
        return len(cards) > 0

    def task_cards_have_titles(self):
        titles = self.find_visible_elements(self.task_titles)
        return all(title.text.strip() for title in titles)

    def select_filter_option(self, filter_locator):
        self.click_element(filter_locator)

        option_locator = (
            By.XPATH,
            "//li[@role='option' and @data-value!='']"
        )

        option = self.find_visible_element(option_locator)

        option_text = option.text.strip()
        option_value = option.get_attribute("data-value")

        self.click_element(option_locator)

        self.wait_for_text_in_element(filter_locator, option_text)

        return option_text, option_value

    def select_assignee_filter(self):
        return self.select_filter_option(self.assignee_filter)

    def select_status_filter(self):
        return self.select_filter_option(self.status_filter)

    def select_label_filter(self):
        return self.select_filter_option(self.label_filter)

    def get_task_columns(self):
        return self.find_visible_elements(self.task_columns)

    def get_column_titles(self):
        columns = self.get_task_columns()

        return [
            column.find_element(
                By.XPATH,
                "./preceding-sibling::h6[1]"
            ).text.strip()
            for column in columns
        ]

    def tasks_are_in_status(self, status_name):
        status_heading = (
            By.XPATH,
            f"//h6[normalize-space()='{status_name}']"
        )

        return self.is_element_visible(status_heading)

    def open_edit_form(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        edit_link = (
            By.XPATH,
            task_card[1] + "//a[@aria-label='Edit']"
        )

        self.click_element(edit_link)

    def task_is_displayed(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        return self.is_element_visible(task_card)

    def filter_by_status(self, status_name):
        self.select_filter_option_by_name(
            self.status_filter,
            status_name
        )

    def select_filter_option_by_name(self, filter_locator, option_name):
        self.click_element(filter_locator)

        option_locator = (
            By.XPATH,
            f"//li[@role='option' "
            f"and normalize-space()='{option_name}']"
        )

        self.click_element(option_locator)

    def task_is_not_displayed(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        return self.wait_until_invisible(task_card)
