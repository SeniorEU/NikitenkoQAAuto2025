from selenium import webdriver # import the Selenium WebDriver browser control | імпортуємо керування браузером Selenium WebDriver
from selenium.webdriver.common.by import By # import the By class to locate elements | імпортуємо клас By для знаходження елементів
from selenium.webdriver.support import expected_conditions as EC # import the expected_conditions module to wait for elements | імпортуємо модуль expected_conditions для очікування елементів
from selenium.webdriver.chrome.service import Service # import the Service class to manage the ChromeDriver service | імпортуємо клас Service для керування службою ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait # import the WebDriverWait class to wait for elements | імпортуємо клас WebDriverWait для очікування елементів    
from selenium.webdriver.chrome.options import Options # import the Options class to set Chrome options | імпортуємо клас Options для налаштування параметрів Chrome
from webdriver_manager.chrome import ChromeDriverManager # import the ChromeDriverManager to manage ChromeDriver installation | імпортуємо ChromeDriverManager для керування установкою ChromeDriver
import time # import the time module to add delays | імпортуємо модуль time для додавання затримок

class RozetkaLoginPage: # Class for Rozetka login page | Клас для сторінки входу Rozetka
    URL = "https://rozetka.com.ua/"

    def __init__(self): # Constructor to initialize the WebDriver and wait | Конструктор для ініціалізації WebDriver та очікування
        options = Options()
        options.add_argument("--disable-gpu")
        options.headless = False

        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 10)
    
    # Implicit wait for elements to be present | Неявне очікування для наявності елементів
    def go_to(self):
        self.driver.get(self.URL)

    # Open login modal and choose email method | Відкриваємо вікно входу та вибираємо метод електронної пошти
    def open_login_modal(self):
        profile_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.header__button"))
        )
        profile_icon.click()
        time.sleep(0.5) # Wait for the login button to be clickable and then click it | Чекаємо, поки кнопка входу стане клікабельною, а потім натискаємо її
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button--small.user-login__button"))
        )
        self.driver.execute_script("arguments[0].click();", login_btn)
        time.sleep(0.5) # Wait for the login modal to appear | Чекаємо, поки з'явиться вікно входу

    # Choose email login method | Вибираємо метод входу через електронну пошту
    def choose_email_login(self):
        other_methods = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Інші способи авторизації')]"))
        )
        other_methods.click()
        time.sleep(0.3)

        # Click on the email login option | Натискаємо на опцію входу через електронну пошту
        email_login = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Увійти через електронну пошту')]"))
        )
        email_login.click()
        time.sleep(0.5)

    # Enter email and password | Вводимо електронну пошту та пароль
    def enter_credentials(self, email, password):
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        time.sleep(0.5)

    # Click the 'Continue' button | Натискаємо кнопку 'Продовжити'
    def submit_login(self):
        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Продовжити')]"))
        )
        # Scroll to the button and click it | Прокручуємо до кнопки та натискаємо її
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(0.5)
        # Click the button using JavaScript to avoid issues with visibility | Натискаємо кнопку за допомогою JavaScript, щоб уникнути проблем з видимістю
        self.driver.execute_script("arguments[0].click();", submit_btn)
        time.sleep(2)
        # так як не з'являється вікно з помилкою, закриваємо вікно
        
    # Close the browser | Закриваємо браузер
    def close(self):
        self.driver.quit()
