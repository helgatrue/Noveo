import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def login():
    username = 'otrofimova'
    password = '602279cb'

    browser = webdriver.Chrome("../chromedriver/chromedriver.exe")
    browser.maximize_window()

    browser.get('http://stage-hr.noveogroup.com/')
    user_input = browser.find_element_by_id("username")
    user_input.send_keys(username)

    password_input = browser.find_element_by_id("password")
    password_input.send_keys(password)

    login_button = browser.find_element_by_name("submit")
    login_button.click()

    change_role = browser.find_element_by_id("username_button")
    change_role.click()

    impersonate = browser.find_element_by_id("impersonate_aluneva")
    impersonate.click()
    timeout = 1
    try:
        element_present = EC.url_contains('http://qa-hr.noveogroup.com/forms')
        WebDriverWait(browser, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")

    browser.get('http://stage-hr.noveogroup.com/candidate/create')

    input_last_name = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
    input_last_name.click()
    input_last_name.send_keys("Петров")

    input_first_name = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
    input_first_name.click()
    input_first_name.send_keys('Иконостас')

    input_middle_name = browser.find_element_by_xpath("//input[@placeholder='Введите отчество']")
    input_middle_name.click()
    input_middle_name.send_keys('Анастасович')

    choose_the_city = browser.find_element_by_xpath("//input[@placeholder='Выберите город']")
    choose_the_city.click()
    choose_the_city.send_keys('Краснодар')

    choose_the_vacansy = browser.find_element_by_xpath("//input[@placeholder='Выберите вакансии']")
    choose_the_vacansy.click()
    choose_the_vacansy.send_keys('Android (СПб, Нск, Краснодар, Казань)')
    choose_the_vacansy.send_keys(Keys.ENTER)

    choose_the_search_source = browser.find_element_by_xpath("//input[@placeholder='Выберите источник поиска']")
    choose_the_search_source.click()
    choose_the_search_source.send_keys('hh.ru direct search')
    choose_the_search_source.send_keys(Keys.DOWN, Keys.ENTER)

    add_watchers = browser.find_element_by_xpath("//input[@placeholder='Добавить наблюдателя']")
    add_watchers.click()
    add_watchers.send_keys('Сотникова Анастасия')
    add_watchers.send_keys(Keys.ENTER)

    input_phone_number = browser.find_element_by_xpath("//input[@placeholder='Введите номер телефона']")
    input_phone_number.click()
    input_phone_number.send_keys('+79002553300')

    input_email = browser.find_element_by_xpath("//input[@placeholder='Введите email']")
    input_email.click()
    input_email.send_keys('abc@gmail.com')

    input_skype = browser.find_element_by_xpath("//input[@placeholder='Введите логин в Skype']")
    input_skype.click()
    input_skype.send_keys('qwerty1234')

    input_telegram = browser.find_element_by_xpath("//input[@placeholder='Введите логин в Telegram']")
    input_telegram.click()
    input_telegram.send_keys('1234qwerty')

    input_linkedin = browser.find_element_by_xpath("//input[@placeholder='Введите адрес страницы в Linkedin']")
    input_linkedin.click()
    input_linkedin.send_keys('linkedin.com')

    input_github = browser.find_element_by_xpath("//input[@placeholder='Введите адрес страницы в Github']")
    input_github.click()
    input_github.send_keys('github.com')

    input_wishing_salary = browser.find_element_by_xpath("//input[@placeholder='Введите желаемую зарплату']")
    input_wishing_salary.click()
    input_wishing_salary.send_keys('100 000')

    input_education = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[3]/div[2]/div/div[1]')
    input_education.click()
    input_education.send_keys('МГУ им М.В. Ломоносова')

    choose_english_level = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[3]/div[1]/div[2]/div/div/span/select')
    choose_english_level.click()
    choose_english_level.send_keys(Keys.DOWN, Keys.ENTER)

    # input_description_hh = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[4]/div/div[2]/div')
    # input_description_hh.click()
    # input_description_hh.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')
    #
    # input_description_habr = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[5]/div/div[2]/div')
    # input_description_habr.click()
    # input_description_habr.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')
    #
    # input_description_linked = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[6]/div/div[2]/div')
    # input_description_linked.click()
    # input_description_linked.send_keys('Смысл сайта/'
    #                                'Сайт рыбатекст поможет дизайнеру, верстальщику, вебмастеру сгенерировать несколько абзацев более менее осмысленного текста рыбы на русском языке, а начинающему оратору отточить навык публичных выступлений в домашних условиях. При создании генератора мы использовали небезизвестный универсальный код речей. Текст генерируется абзацами случайным образом от двух до десяти предложений в абзаце, что позволяет сделать текст более привлекательным и живым для визуально-слухового восприятия./'
    #                                'По своей сути рыбатекст является альтернативой традиционному lorem ipsum, который вызывает у некторых людей недоумение при попытках прочитать рыбу текст. В отличии от lorem ipsum, текст рыба на русском языке наполнит любой макет непонятным смыслом и придаст неповторимый колорит советских времен.')

    click_btn_save = browser.find_element_by_xpath('//*[@id="app"]/div/div/section/div/form/div[8]/span/button')
    click_btn_save.click()

    browser.get('http://stage-hr.noveogroup.com/candidate/list')

    # go_to_candidate_list = browser.find_element_by_xpath('//*[@id="candidate_list_link"]')
    # go_to_candidate_list.click()

    time.sleep(2)
    # try:
    #     element_present = EC.url_contains('http://stage-hr.noveogroup.com/candidate/list')
    #     WebDriverWait(browser, timeout).until(element_present)
    # except TimeoutException:
    #     print("Timed out waiting for page to load")
    # finally:
    #     print("Page loaded")

    # find_candidate = browser.find_element_by_xpath("//input[@placeholder='Искать...']")
    # find_candidate.click()
    # find_candidate.send_keys('Анастасович')


if __name__ == '__main__':
    login()
    quit()
