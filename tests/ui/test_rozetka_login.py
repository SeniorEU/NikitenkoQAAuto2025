import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.ui
def test_rozetka_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://rozetka.com.ua/")

    try:
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header__button"))).click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button--small.user-login__button"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Інші способи авторизації')]"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Увійти через електронну пошту')]"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("ua.middle@gmail.com")
        driver.find_element(By.ID, "password").send_keys("wrong password")

        # Натискаємо кнопку
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Продовжити')]")))
        driver.execute_script("arguments[0].click();", btn)

        # Вивід HTML всієї сторінки
        print("\n\n======= PAGE HTML =======")
        print(driver.page_source)
        print("======= END OF PAGE =====\n\n")

    finally:
        driver.quit()