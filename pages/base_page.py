from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, base_url=None):
        self.browser = browser
        self.base_url = base_url

    def open_url(self, url):
        self.browser.get(url)

    def find_visible_element(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        self.find_visible_element(locator).send_keys(text)

    def get_element_text(self, locator):
        return self.find_visible_element(locator).text

    def is_element_visible(self, locator):
        return self.find_visible_element(locator).is_displayed()

    def wait_until_invisible(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_field_to_be_empty(self, field):
        return WebDriverWait(self.browser, 5).until(
            lambda browser: field.get_attribute("value") == ""
        )

    def wait_for_attribute(self, locator, attribute, value):
        return WebDriverWait(self.browser, 5).until(
            lambda browser: (
                browser.find_element(*locator).get_attribute(attribute) == value
            )
        )

    def find_visible_elements(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def find_any_visible_elements(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_any_elements_located(locator)
        )

    def wait_for_text_in_element(self, locator, text):
        return WebDriverWait(self.browser, 5).until(
            lambda browser: text in browser.find_element(*locator).text
        )
