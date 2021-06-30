from selenium import webdriver
import time
from Log_In.locators import LogIn


def input_username(self, username):
    input_user_name = self.browser.find_element(*LogIn.USER_NAME)
    input_user_name.click()
    input_user_name.send_keys(username)


def new():
    browser = webdriver.Chrome()
    # change_user = ChangeUser(browser, browser.current_url)
    # change_user.change_role_click()

    # browser.find_element_by_id("username_button").click()
    # time.sleep(1)
    # browser.find_element_by_id("impersonate_aluneva").click()
    # time.sleep(1)

    # browser.find_element_by_id("browser.find_element_by_id").click()
    browser.get("http://stage-hr.noveogroup.com/candidate/create")

    # last_name = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/form/div[1]/div/div[1]/div[1]/div/input')
    # last_name.click()
    # last_name.send_keys("Иванов")
    # first_name = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/form/div[1]/div/div[1]/div[2]/div/input')
    # first_name.click()
    # first_name.send_keys("Иван")
    # choose_the_vacansy = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/form/div[1]/div/div[2]/div[1]/div/div/div/div[1]/input')
    # choose_the_vacansy.click()
    # choose_the_vacansy.send_keys('Android SPB')
    # choose_the_vacansy.send_keys(Keys.ENTER)
    #
    # browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[6]/span/button').click()
    #
    # time.sleep(1)
    #
    # browser.get("http://stage-hr.noveogroup.com/candidate/list")
    #
    # browser.get("http://stage-hr.noveogroup.com/candidate/")
    #
    # more_info_btn = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/div/div/div/section/div[1]/section/div/div/table/tbody/tr/td[7]/div/span[1]/a')
    # more_info_btn.click()
    #
    # edit_btn = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/div/div/div/section/div[1]/section/div[1]/div[2]/div/form/div/section/div/div[1]/div/button/span/span')
    # edit_btn.click()
    #
    # status_btn = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/div/div/div/section/div[1]/section/div[1]/div[2]/div/form/div/section/div/div[1]/div/div[2]/div/span/select')
    # status_btn.click()
    #
    # status_selection = browser.find_element_by_xpath(
    #     '//*[@id="app"]/div/div/section/div/div/div/div/section/div[1]/section/div[1]/div[2]/div/form/div/section/div/div[1]/div/div[2]/div/span/select/option[6]')
    # status_selection.click()

    time.sleep(1)
