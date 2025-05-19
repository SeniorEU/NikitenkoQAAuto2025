# test file for UI
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Create an object to control the browser
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page https://github.com/login
    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")
    
    # We find a login field and a false username or email address
    # Знаходимо поле для введення логіна та хибне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # Entering a false username or mailing address
    # Вводимо хибне ім'я користувача або поштову адресу
    login_elem.send_keys("ivan.nikitenko@mistakeinemail.com")

    # Find the field where we will enter the false password
    # Знаходимо поле, в якому будемо вводити хибний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Entering a wrong password
    # Вводимо хибний пароль
    pass_elem.send_keys("wrong password")

    # Find the “Sign in” button
    # Знаходимо кнопку "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")
    
    # Click (emulate a left-click) on the “Sign in” button
    # Клікаємо (ємулюємо клік лівої кнопки миші) на кнопку "Sign in"
    btn_elem.click()
    
    # Check that the page title is the same as we expect
    # Перевіряємо, що назва сторінки така сама, яку ми і очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"

    # Close the browser
    # Закриваємо браузер
    driver.close()