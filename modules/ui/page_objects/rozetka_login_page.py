from selenium import webdriver # import the Selenium WebDriver browser control 
from selenium.webdriver.common.by import By # import the By class to locate elements 
from selenium.webdriver.support import expected_conditions as EC # import the expected_conditions module to wait for elements 
from selenium.webdriver.chrome.service import Service # import the Service class to manage the ChromeDriver service 
from selenium.webdriver.support.ui import WebDriverWait # import the WebDriverWait class to wait for elements 
from selenium.webdriver.chrome.options import Options # import the Options class to set Chrome options 
from webdriver_manager.chrome import ChromeDriverManager # import the ChromeDriverManager to manage ChromeDriver installation 
import time # import the time module to add delays 

class RozetkaLoginPage: # Class for Rozetka login page 
    URL = "https://rozetka.com.ua/"

    def __init__(self): # Constructor to initialize the WebDriver and wait 
        options = Options()
        options.add_argument("--disable-gpu")
        options.headless = False

        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    # Implicit wait for elements to be present
    def go_to(self):
        self.driver.get(self.URL)

    # Open login modal and choose email method
    def open_login_modal(self):
        profile_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header__button"))
        )
        profile_icon.click()
        time.sleep(0.5) # Wait for the login button to be clickable and then click it
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button--small.user-login__button"))
        )
        self.driver.execute_script("arguments[0].click();", login_btn)
        time.sleep(0.5) # Wait for the login modal to appear

    # Choose email login method
    def choose_email_login(self):
        other_methods = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Інші способи авторизації')]"))
        )
        other_methods.click()
        time.sleep(0.3)

        # Click on the email login option 
        email_login = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Увійти через електронну пошту')]"))
        )
        email_login.click()
        time.sleep(0.5)

    # Enter email and password 
    def enter_credentials(self, email, password):
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        time.sleep(0.5)

    # Click the 'Continue' button 
    def submit_login(self):
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Продовжити')]"))
        )
        # Scroll to the button and click it
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(0.5)
        # Click the button using JavaScript to avoid issues with visibility
        self.driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(2)
        
    # Close the browser
    def close(self):
        self.driver.quit()
