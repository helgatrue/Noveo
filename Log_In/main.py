import time

from locators import LogIn, SelectUser, CandidateCreation, CandidateList
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_candidate_requirement_fields(browser):
    username = 'otrofimova'
    password = '602279cb'

    browser.get('http://stage-hr.noveogroup.com/')
    user_input = browser.find_element(*LogIn.USER_NAME)
    user_input.send_keys(username)

    password_input = browser.find_element(*LogIn.PASSWORD)
    password_input.send_keys(password)

    login_button = browser.find_element(*LogIn.SUBMIT_BTN)
    login_button.click()

    change_role = browser.find_element(*SelectUser.USER_LIST)
    change_role.click()

    impersonate = browser.find_element(*SelectUser.USER_LUNEVA)
    impersonate.click()
    timeout = 2
    try:
        element_present = EC.url_contains('http://stage-hr.noveogroup.com/forms')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page http://stage-hr.noveogroup.com/forms is loaded")

    browser.get('http://stage-hr.noveogroup.com/candidate/create')

    input_last_name = browser.find_element(*CandidateCreation.CANDIDATE_LAST_NAME)
    input_last_name.click()
    input_last_name.send_keys("Растропович")

    input_first_name = browser.find_element(*CandidateCreation.CANDIDATE_FIRST_NAME)
    input_first_name.click()
    input_first_name.send_keys('Альберт')

    click_btn_save = browser.find_element(*CandidateCreation.CANDIDATE_CREATE_BTN)
    click_btn_save.click()
    timeout = 2
    try:
        element_present = EC.url_contains(
            'http://stage-hr.noveogroup.com/vacancy/129/candidate-processings?vacancy_processing=27649')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print(
            "Page http://stage-hr.noveogroup.com/vacancy/129/candidate-processings?vacancy_processing=27649 is loaded")

    go_to_candidate_list = browser.find_element(*CandidateList.CANDIDATE_LIST_TAB)
    go_to_candidate_list.click()
    timeout = 2
    try:
        element_present = EC.url_contains('http://stage-hr.noveogroup.com/candidate/list')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page http://stage-hr.noveogroup.com/candidate/list is loaded")

    find_candidate = browser.find_element(*CandidateList.CANDIDATE_LIST_SEARCH_NAME)
    find_candidate.click()
    find_candidate.send_keys('Растропович')

    amount_of_candidates = len(browser.find_elements_by_xpath("//*[contains(text(), 'Растропович')]"))
    if amount_of_candidates > 0:
        print("Element Анастасович exists")
        print("Растроповичей: " + str(amount_of_candidates))
    else:
        print('Element Анастасович is not found')


def test_create_optional_fields(browser):
    username = 'otrofimova'
    password = '602279cb'

    browser.get('http://qa-hr.noveogroup.com/')
    user_input = browser.find_element(*LogIn.USER_NAME)
    user_input.send_keys(username)

    password_input = browser.find_element(*LogIn.PASSWORD)
    password_input.send_keys(password)

    login_button = browser.find_element(*LogIn.SUBMIT_BTN)
    login_button.click()

    change_role = browser.find_element(*SelectUser.USER_LIST)
    change_role.click()

    impersonate = browser.find_element(*SelectUser.USER_LUNEVA)
    impersonate.click()
    time.sleep(5)
    timeout = 10
    try:
        element_present = EC.url_contains('http://qa-hr.noveogroup.com/forms')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page http://qa-hr.noveogroup.com/forms is loaded")

    browser.get('http://qa-hr.noveogroup.com/candidate/create')

    input_last_name = browser.find_element(*CandidateCreation.CANDIDATE_LAST_NAME)
    input_last_name.click()
    input_last_name.send_keys("Петров")

    input_first_name = browser.find_element(*CandidateCreation.CANDIDATE_FIRST_NAME)
    input_first_name.click()
    input_first_name.send_keys('Иконостас')

    input_middle_name = browser.find_element(*CandidateCreation.CANDIDATE_MIDDLE_NAME)
    input_middle_name.click()
    input_middle_name.send_keys('Анастасович')

    choose_the_city = browser.find_element(*CandidateCreation.CANDIDATE_CITY)
    choose_the_city.click()
    choose_the_city.send_keys('Краснодар')

    choose_the_vacancy = browser.find_element(*CandidateCreation.CANDIDATE_VACANCY)
    choose_the_vacancy.click()
    choose_the_vacancy.send_keys('Android (СПб, Нск, Краснодар, Казань)')
    choose_the_vacancy.send_keys(Keys.ENTER)

    choose_the_search_source = browser.find_element(*CandidateCreation.CANDIDATE_THE_SEARCH_SOURCE)
    choose_the_search_source.click()
    choose_the_search_source.send_keys('hh.ru direct search')
    choose_the_search_source.send_keys(Keys.DOWN, Keys.ENTER)

    add_watchers = browser.find_element(*CandidateCreation.CANDIDATE_ADD_WATCHERS)
    add_watchers.click()
    add_watchers.send_keys('Сотникова Анастасия')
    add_watchers.send_keys(Keys.ENTER)

    input_phone_number = browser.find_element(*CandidateCreation.CANDIDATE_PHONE_NUMBER)
    input_phone_number.click()
    input_phone_number.send_keys('+79002553300')

    input_email = browser.find_element(*CandidateCreation.CANDIDATE_EMAIL)
    input_email.click()
    input_email.send_keys('abc@gmail.com')

    input_skype = browser.find_element(*CandidateCreation.CANDIDATE_SKYPE)
    input_skype.click()
    input_skype.send_keys('qwerty1234')

    input_telegram = browser.find_element(*CandidateCreation.CANDIDATE_TELEGRAM)
    input_telegram.click()
    input_telegram.send_keys('1234qwerty')

    input_linkedin = browser.find_element(*CandidateCreation.CANDIDATE_LINKEDIN)
    input_linkedin.click()
    input_linkedin.send_keys('linkedin.com')

    input_github = browser.find_element(*CandidateCreation.CANDIDATE_GITHUB)
    input_github.click()
    input_github.send_keys('github.com')

    input_wishing_salary = browser.find_element(*CandidateCreation.CANDIDATE_WISHING_SALARY)
    input_wishing_salary.click()
    input_wishing_salary.send_keys('100 000')

    input_education = browser.find_element(*CandidateCreation.CANDIDATE_EDUCATION)
    input_education.click()
    input_education.send_keys('МГУ им М.В. Ломоносова')

    choose_english_level = browser.find_element(*CandidateCreation.CANDIDATE_ENGLISH_LEVEL)
    choose_english_level.click()
    choose_english_level.send_keys(Keys.DOWN, Keys.ENTER)

    input_description_hh = browser.find_element(*CandidateCreation.CANDIDATE_INPUT_DESCRIPTION_HH)
    input_description_hh.click()
    input_description_hh.send_keys('Привет')

    click_btn_save = browser.find_element(*CandidateCreation.CANDIDATE_CREATE_BTN)
    click_btn_save.click()
    timeout = 2
    try:
        element_present = EC.url_contains(
            'http://qa-hr.noveogroup.com/vacancy/129/candidate-processings?vacancy_processing=27649')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print(
            "Page http://qa-hr.noveogroup.com/vacancy/129/candidate-processings?vacancy_processing=27649 is loaded")

    go_to_candidate_list = browser.find_element(*CandidateList.CANDIDATE_LIST_TAB)
    go_to_candidate_list.click()
    timeout = 2
    try:
        element_present = EC.url_contains('http://qa-hr.noveogroup.com/candidate/list')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page http://qa-hr.noveogroup.com/candidate/list is loaded")

    find_candidate = browser.find_element(*CandidateList.CANDIDATE_LIST_SEARCH_NAME)
    find_candidate.click()
    find_candidate.send_keys('Анастасович')

    amount_of_candidates = len(browser.find_elements_by_xpath("//*[contains(text(), 'Анастасович')]"))
    if amount_of_candidates > 0:
        print("Element Анастасович exists")
        print("Анастасовичей: " + str(amount_of_candidates))
    else:
        print('Element Анастасович is not found')


if __name__ == '__main__':
    test_create_candidate_requirement_fields()
    test_create_optional_fields()
    quit()
