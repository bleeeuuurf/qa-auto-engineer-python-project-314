from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TasksPage:
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
    task_cards = (By.CSS_SELECTOR, "[data-rfd-draggable-id]")

    task_cards = (
        By.CSS_SELECTOR,
        "div[data-rfd-draggable-id]"
    )

    task_titles = (
        By.CSS_SELECTOR,
        "div[data-rfd-draggable-id] .MuiTypography-h5"
    )

    edit_button = (By.CSS_SELECTOR, 'a[aria-label="Edit"]') 

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def open_page(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.tasks_menu_item)
        ).click()

    def board_is_loaded(self):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_any_elements_located(self.task_columns)
        )

    def open_create_form(self):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def task_is_in_column(self, title, status_id):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-droppable-id='{status_id}']"
            f"//div[@data-rfd-draggable-id]"
            f"[.//*[normalize-space()='{title}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(task_card)
        ).is_displayed()

    def tasks_are_displayed(self):
        cards = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.task_cards)
        )

        return all(card.is_displayed() for card in cards)


    def task_cards_have_titles(self):
        cards = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.task_cards)
        )

        return all(
            card.find_element(
                By.CSS_SELECTOR, ".MuiTypography-h5"
            ).text.strip()
            for card in cards
        )


    def select_filter_option(self, filter_locator):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(filter_locator)
        ).click()

        option_locator = (
            By.XPATH,
            "//li[@role='option' and @data-value!='']"
        )

        option = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(option_locator)
        )

        option_text = option.text.strip()
        option_value = option.get_attribute("data-value")

        option.click()

        WebDriverWait(self.browser, 5).until(
            lambda browser: option_text in
            browser.find_element(*filter_locator).text
        )

        return option_text, option_value


    def select_assignee_filter(self):
        return self.select_filter_option(self.assignee_filter)


    def select_status_filter(self):
        return self.select_filter_option(self.status_filter)


    def select_label_filter(self):
        return self.select_filter_option(self.label_filter)

    def tasks_are_displayed(self):
        cards = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.task_cards)
        )
        return len(cards) > 0


    def task_cards_have_titles(self):
        titles = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.task_titles)
        )
        return all(title.text.strip() for title in titles)

    def get_task_columns(self):
        columns = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(self.task_columns)
        )

        return columns


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

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(status_heading)
        ).is_displayed()

    def open_edit_form(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        card = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(task_card)
        )

        card.find_element(*self.edit_button).click()

    def task_is_displayed(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(task_card)
        ).is_displayed()

    def filter_by_status(self, status_name):
        self.select_filter_option_by_name(
            self.status_filter,
            status_name
        )

    def select_filter_option_by_name(self, filter_locator, option_name):
        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(filter_locator)
        ).click()

        option_locator = (
            By.XPATH,
            f"//li[@role='option' "
            f"and normalize-space()='{option_name}']"
        )

        WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(option_locator)
        ).click()

    def task_is_not_displayed(self, title):
        task_card = (
            By.XPATH,
            f"//div[@data-rfd-draggable-id]"
            f"[.//div[contains(@class, 'MuiTypography-h5') "
            f"and normalize-space()='{title}']]"
        )

        return WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(task_card)
        )