import pytest
from selenium.webdriver.common.by import By
import time 

@pytest.mark.parametrize('id, link', [
    pytest.param('bx_1847241719_42', "https://z51.ru/catalog/kresla/", id="Игровые кресла"),
    pytest.param('bx_1847241719_67', "https://z51.ru/catalog/ergonomic-office-chairs/", id="Эргономичные кресла"), 
    pytest.param('bx_1847241719_48', "https://z51.ru/catalog/desks/", id="Игровые столы"), 
    pytest.param('bx_1847241719_41', "https://z51.ru/catalog/garnitury/", id="Гарнитуры"), 
    pytest.param('bx_1847241719_44', "https://z51.ru/catalog/keyboards/", id="Клавиатуры"), 
    pytest.param('bx_1847241719_45', "https://z51.ru/catalog/mice/", id="Мыши"), 
    pytest.param('bx_1847241719_63', "https://z51.ru/catalog/gaming-pc/", id="Игровые ПК"), 
    pytest.param('bx_1847241719_43', "https://z51.ru/catalog/aksessuary/", id="Аксессуары"), 
    pytest.param('bx_1847241719_49', "https://z51.ru/catalog/components/", id="Комплектующие для кресел")
    ])
def test_categories(browser, id, link):
    category = browser.find_element(By.CSS_SELECTOR, f'div[id={id}]>a')
    category.click()
    time.sleep(2)
    assert browser.current_url == link
    browser.back()
    time.sleep(2)
        