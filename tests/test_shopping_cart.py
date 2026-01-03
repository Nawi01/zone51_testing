import pytest
from selenium.webdriver.common.by import By
import time 
from selenium.common.exceptions import NoSuchElementException

def sleep(): #используется только для визуальной оценки происходящего
    time.sleep(2)

all_categories = ['bx_1847241719_42', 'bx_1847241719_67', 'bx_1847241719_48', 'bx_1847241719_41', 'bx_1847241719_44', 'bx_1847241719_45', 'bx_1847241719_43', 'bx_1847241719_49']

def test_shopping_cart(browser):
    for category in all_categories:
        browser.find_element(By.CSS_SELECTOR, f'div[id={category}]>a').click()
        sleep()
        try: 
            browser.find_element(By.CSS_SELECTOR, 'button[data-action="addToBasket"]').click()#Будет найден и добавлен только первый товар с кнопкой "В корзину"
            browser.find_element(By.CSS_SELECTOR, 'button[aria-label="Close"]').click()#Закрываем всплывающее окно
            browser.back()
            sleep()
        except NoSuchElementException: 
            browser.back()
    browser.find_element(By.CLASS_NAME, 'zone__header__cart').click() #Корзина
    sleep()
    #Прокрутка страницы
    # height = browser.execute_script("return document.body.scrollHeight")
    # for i in range(0, height, 50):
    #     browser.execute_script(f"window.scrollTo(0, {i})")