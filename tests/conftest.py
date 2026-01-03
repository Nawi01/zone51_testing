import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications") # Отключает уведомления
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2, # 2 = Заблокировать
    "profile.default_content_setting_values.popups": 2 # Блокирует и pop-ups
})

link = "https://z51.ru/"
@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)
    yield browser
    browser.quit()