# test file for UI
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    # Знаходимо поле для введення логіна та хибне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо хибне ім'я користувача або поштову адресу
    login_elem.send_keys("ivan.nikitenko@mistakeinemail.com")

    # Знаходимо поле, в якому будемо вводити хибний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо хибний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")

    # Клікаємо (ємулюємо клік лівої кнопки миші) на кнопку "Sign in"
    btn_elem.click()

    # Перевіряємо, що назва сторінки така сама, яку ми і очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Закриваємо браузер
    driver.close()