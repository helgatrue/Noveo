from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def _is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def _is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def url_is_valid(self, page_url):
        current_url = self.browser.current_url
        assert page_url in current_url, f'Текущий URL = "{current_url}", не содержит "{page_url}"'

    def _get_element_text(self, how, what):
        return self.browser.find_element(how, what).text

    def _get_attribute(self, how, what, attr):
        return self.browser.find_element(how, what).get_attribute(attr)

    def _get_value_of_css_property(self, how, what, value):
        return self.browser.find_element(how, what).value_of_css_property(value)