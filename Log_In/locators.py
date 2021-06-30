from selenium.webdriver.common.by import By


class LogIn:
    USER_NAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BTN = (By.TAG_NAME, "#submit")


class SelectUser:
    USER_LIST = (By.ID, "#username_button")
    USER_LUNEVA = (By.ID, "#impersonate_aluneva")



