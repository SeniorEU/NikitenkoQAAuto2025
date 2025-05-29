# test file for UI
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Create an object to control the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # open the page https://github.com/login
    driver.get("https://github.com/login")
    
    # We find a login field and a false username or email address
    login_elem = driver.find_element(By.ID, "login_field")

    # Entering a false username or mailing address
    login_elem.send_keys("ivan.nikitenko@mistakeinemail.com")

    # Find the field where we will enter the false password
    pass_elem = driver.find_element(By.ID, "password")

    # Entering a wrong password
    pass_elem.send_keys("wrong password")

    # Find the “Sign in” button
    btn_elem = driver.find_element(By.NAME, "commit")
    
    # Click (emulate a left-click) on the “Sign in” button
    btn_elem.click()
    
    # Check that the page title is the same as we expect
    assert driver.title == "Sign in to GitHub · GitHub"

    # Close the browser
    driver.close()