from selenium.webdriver.common.by import By


class LogIn:
    USER_NAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BTN = (By.CSS_SELECTOR, "[name= 'submit']")


class SelectUser:
    USER_LIST = (By.CSS_SELECTOR, "#username_button")
    USER_LUNEVA = (By.CSS_SELECTOR, "#impersonate_aluneva")


class CandidateCreation:
    CANDIDATE_LAST_NAME = (By.XPATH, "//input[@placeholder='Введите фамилию']")
    CANDIDATE_FIRST_NAME = (By.XPATH, "//input[@placeholder='Введите имя']")
    CANDIDATE_MIDDLE_NAME = (By.XPATH, "//input[@placeholder='Введите отчество']")
    CANDIDATE_CITY = (By.XPATH, "//input[@placeholder='Выберите город']")
    CANDIDATE_VACANCY = (By.XPATH, "//input[@placeholder='Выберите вакансии']")
    CANDIDATE_THE_SEARCH_SOURCE = (By.XPATH, "//input[@placeholder='Выберите источник поиска']")
    CANDIDATE_ADD_WATCHERS = (By.XPATH, "//input[@placeholder='Добавить наблюдателя']")
    CANDIDATE_PHONE_NUMBER = (By.XPATH, "//input[@placeholder='Введите номер телефона']")
    CANDIDATE_EMAIL = (By.XPATH, "//input[@placeholder='Введите email']")
    CANDIDATE_SKYPE = (By.XPATH, "//input[@placeholder='Введите логин в Skype']")
    CANDIDATE_TELEGRAM = (By.XPATH, "//input[@placeholder='Введите логин в Telegram']")
    CANDIDATE_LINKEDIN = (By.XPATH, "//input[@placeholder='Введите адрес страницы в Linkedin']")
    CANDIDATE_GITHUB = (By.XPATH, "//input[@placeholder='Введите адрес страницы в Github']")
    CANDIDATE_WISHING_SALARY = (By.XPATH, "//input[@placeholder='Введите желаемую зарплату']")
    CANDIDATE_EDUCATION = (By.XPATH, "//*[@id='app']/div/div/section/div/form/div[3]/div[2]/div/div[1]")
    CANDIDATE_ENGLISH_LEVEL = (
    By.XPATH, '//*[@id="app"]/div/div/section/div/form/div[3]/div[1]/div[2]/div/div/span/select')

    CANDIDATE_INPUT_DESCRIPTION_HH = (By.XPATH, '//*[@id="app"]/div/div/section/div/form/div[4]/div/div[2]/div')
    CANDIDATE_INPUT_DESCRIPTION_HABR = (By.XPATH, '//*[@id="app"]/div/div/section/div/form/div[5]/div/div[2]/div')
    CANDIDATE_INPUT_DESCRIPTION_LINKEDIN = (By.XPATH, '//*[@id="app"]/div/div/section/div/form/div[6]/div/div[2]/div')

    CANDIDATE_CREATE_BTN = (By.CSS_SELECTOR, '.is-success > span')


class CandidateList:
    CANDIDATE_LIST_TAB = (By.XPATH, '//a[@href="http://stage-hr.noveogroup.com/candidate/list"]')
    CANDIDATE_LIST_SEARCH_NAME = (By.XPATH, "//input[@placeholder='Искать...']")
