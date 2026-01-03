import pytest
from selenium.webdriver.common.by import By
import time 

def sleep(): #используется только для визуальной оценки происходящего
    time.sleep(2)

all_categories = ['bx_1847241719_42', 'bx_1847241719_67', 'bx_1847241719_48', 'bx_1847241719_41', 'bx_1847241719_44', 'bx_1847241719_45', 'bx_1847241719_63', 'bx_1847241719_43', 'bx_1847241719_49']

def test_favorites_button(browser):
    for category in all_categories:
        browser.find_element(By.CSS_SELECTOR, f'div[id={category}]>a').click()
        sleep()
        browser.find_element(By.CSS_SELECTOR, 'button[title="В избранное"]').click() #Будет найден и добавлен только первый товар с кнопкой "В избранное"
        browser.back()
        sleep()
    browser.find_element(By.ID, 'awelite_favorites_equation').click() #Все избранные товары
    sleep()
    browser.find_element(By.CSS_SELECTOR, "div[class='clear-favs-button-wrapper'] > a[class='button-remove']").click() #Кнопка очистки избранных товаров
    sleep()
    browser.back()