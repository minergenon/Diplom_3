import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Urls


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    elif request.param == 'chrome':
        options = Options()
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
