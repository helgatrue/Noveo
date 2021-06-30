import os
import sys
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.append('pages')
sys.path.append('const')
sys.dont_write_bytecode = True


def pytest_addoption(parser):
    parser.addoption('--server', action='store', default='203', help='Specify server: 202, 203, 122')
    parser.addoption('--repeat', action='store', help='Number of times to repeat each test')


capabilities = {
    "browserName": "chrome",
    "browserVersion": "89.0",
    "enableVideo": True,
    # "videoName": "video.mp4",
    "enableVNC": True
    # "platform": "LINUX"
}


@pytest.fixture(scope='class')
def browser(chrome_options):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        browser = webdriver.Chrome(options=chrome_options)
        browser.maximize_window()
        # browser.execute_script("document.body.style.zoom='zoom 125%'")
        yield browser
        browser.quit()


@pytest.fixture(scope='session')
def base_url(request):
    base_url = "http://http://qa-hr.noveogroup.com/"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture(scope="class", autouse=True)
def add_video_in_allure_report(request, browser):
    def end():
        video_url = 'http://127.0.0.1:4444/video/'
        html = f"""
        <html><body><video width = '100%'
                           height = '100%'
                           controls
                           autoplay>
                           <source src = '{video_url}{browser.session_id}.mp4'
                                   type='video/mp4'>
        </video></body></html>
        """
        allure.attach(body=html, name="VIDEO", attachment_type=allure.attachment_type.HTML)

    request.addfinalizer(end)


def pytest_generate_tests(metafunc):
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)
        metafunc.fixturenames.append('tmp_ct')
        metafunc.parametrize('tmp_ct', range(count))
