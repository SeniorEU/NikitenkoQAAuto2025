from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# Create a SignInPage class with inheritance from BasePage
# Створюємо клас SignInPage з наслідуваням BasePage
class SignInPage(BasePage): 
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    # Open the GitHub login page in your browser
    # Відкриваємо сторінку логіну GitHub у браузері
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find the ID login field, where we will enter a false username or email
        # Знаходимо поле логіну ID, в яке будемо вводити хибне ім'я користувача або емайл
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Вводимо хибне ім'я користувача або недійсну поштову адресу
        login_elem.send_keys(username)

        # Find the field where we will enter the wrong password
        # Знаходимо поле, в яке будемо вводити хибний пароль
        pass_elem = self.driver.find_element(By.ID, "password")
        
        # Enter the wrong password
        # Вводимо хибний пароль
        pass_elem.send_keys(password)

        # Find the “Sign in” button
        # Знаходимо кнопку входу "Sign in"
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Click (emulate a click) with the left mouse button
        # Клікаємо (ємулюємо клік) лівою кнопкою мишки
        btn_elem.click()
        
    # check if we are on the “Sign in to GitHub - GitHub” page
    # перевіряємо, чи ми на сторінці "Sign in to GitHub · GitHub"
    def check_title(self, expected_title):
        return self.driver.title == expected_title