from base_page import BasePage
from locators import SelectUser


class ChangeUser(BasePage):
    def change_role_click(self):
        username_btn = self.browser.find_element_by_id(*SelectUser.USER_LIST)
        username_btn.click()
        impersonate_btn = self.browser.find_element_by_id(*SelectUser.USER_LUNEVA)
        impersonate_btn.click()
