import time
import base_page
import self as self

from locators import LogIn, SelectUser, CandidateCreation, CandidateList
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def login():
    username = 'otrofimova'
    password = '602279cb'

    driver = webdriver.Chrome("../chromedriver/chromedriver.exe")
    driver.maximize_window()

    driver.get('http://stage-hr.noveogroup.com/')
    user_input = driver.find_element(*LogIn.USER_NAME)
    user_input.send_keys(username)

    password_input = driver.find_element(*LogIn.PASSWORD)
    password_input.send_keys(password)

    login_button = driver.find_element(*LogIn.SUBMIT_BTN)
    login_button.click()

    change_role = driver.find_element(*SelectUser.USER_LIST)
    change_role.click()

    impersonate = driver.find_element(*SelectUser.USER_LUNEVA)
    impersonate.click()
    timeout = 1
    try:
        element_present = EC.url_contains('http://qa-hr.noveogroup.com/forms')
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    driver.get('http://stage-hr.noveogroup.com/candidate/create')

    input_last_name = driver.find_element(*CandidateCreation.CANDIDATE_LAST_NAME)
    input_last_name.click()
    input_last_name.send_keys("Петров")

    input_first_name = driver.find_element(*CandidateCreation.CANDIDATE_FIRST_NAME)
    input_first_name.click()
    input_first_name.send_keys('Иконостас')

    input_middle_name = driver.find_element(*CandidateCreation.CANDIDATE_MIDDLE_NAME)
    input_middle_name.click()
    input_middle_name.send_keys('Анастасович')

    choose_the_city = driver.find_element(*CandidateCreation.CANDIDATE_CITY)
    choose_the_city.click()
    choose_the_city.send_keys('Краснодар')

    choose_the_vacancy = driver.find_element(*CandidateCreation.CANDIDATE_VACANCY)
    choose_the_vacancy.click()
    choose_the_vacancy.send_keys('Android (СПб, Нск, Краснодар, Казань)')
    choose_the_vacancy.send_keys(Keys.ENTER)

    choose_the_search_source = driver.find_element(*CandidateCreation.CANDIDATE_THE_SEARCH_SOURCE)
    choose_the_search_source.click()
    choose_the_search_source.send_keys('hh.ru direct search')
    choose_the_search_source.send_keys(Keys.DOWN, Keys.ENTER)

    add_watchers = driver.find_element(*CandidateCreation.CANDIDATE_ADD_WATCHERS)
    add_watchers.click()
    add_watchers.send_keys('Сотникова Анастасия')
    add_watchers.send_keys(Keys.ENTER)

    input_phone_number = driver.find_element(*CandidateCreation.CANDIDATE_PHONE_NUMBER)
    input_phone_number.click()
    input_phone_number.send_keys('+79002553300')

    input_email = driver.find_element(*CandidateCreation.CANDIDATE_EMAIL)
    input_email.click()
    input_email.send_keys('abc@gmail.com')

    input_skype = driver.find_element(*CandidateCreation.CANDIDATE_SKYPE)
    input_skype.click()
    input_skype.send_keys('qwerty1234')

    input_telegram = driver.find_element(*CandidateCreation.CANDIDATE_TELEGRAM)
    input_telegram.click()
    input_telegram.send_keys('1234qwerty')

    input_linkedin = driver.find_element(*CandidateCreation.CANDIDATE_LINKEDIN)
    input_linkedin.click()
    input_linkedin.send_keys('linkedin.com')

    input_github = driver.find_element(*CandidateCreation.CANDIDATE_GITHUB)
    input_github.click()
    input_github.send_keys('github.com')

    input_wishing_salary = driver.find_element(*CandidateCreation.CANDIDATE_WISHING_SALARY)
    input_wishing_salary.click()
    input_wishing_salary.send_keys('100 000')

    input_education = driver.find_element(*CandidateCreation.CANDIDATE_EDUCATION)
    input_education.click()
    input_education.send_keys('МГУ им М.В. Ломоносова')

    choose_english_level = driver.find_element(*CandidateCreation.CANDIDATE_ENGLISH_LEVEL)
    choose_english_level.click()
    choose_english_level.send_keys(Keys.DOWN, Keys.ENTER)

    # input_description_hh = driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[4]/div/div[2]/div')
    # input_description_hh.click()
    # input_description_hh.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')
    #
    # input_description_habr = driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[5]/div/div[2]/div')
    # input_description_habr.click()
    # input_description_habr.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')
    #
    # input_description_linked = driver.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[6]/div/div[2]/div')
    # input_description_linked.click()
    # input_description_linked.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')

    click_btn_save = driver.find_element(*CandidateCreation.CANDIDATE_CREATE_BTN)
    click_btn_save.click()
    timeout = 2
    try:
        element_present = EC.url_contains('http://stage-hr.noveogroup.com/vacancy/129/candidate-processings?vacancy_processing=27649')
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    go_to_candidate_list = driver.find_element(*CandidateList.CANDIDATE_LIST_TAB)
    go_to_candidate_list.click()
    timeout = 2
    try:
        element_present = EC.url_contains('http://stage-hr.noveogroup.com/candidate/list')
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    find_candidate = driver.find_element(*CandidateList.CANDIDATE_LIST_SEARCH_NAME)
    find_candidate.click()
    find_candidate.send_keys('Анастасович')

    time.sleep(2)

    assert self._is_element_present(*CandidateList.CANDIDATE_LIST_SEARCH_NAME), \
        'Не удалось найти поле ИНН контрагента'


if __name__ == '__main__':
    login()
    quit()
