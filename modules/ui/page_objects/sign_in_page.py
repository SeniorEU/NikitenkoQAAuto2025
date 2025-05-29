from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

# Create a SignInPage class with inheritance from BasePage
class SignInPage(BasePage): 
    URL = 'https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    # Open the GitHub login page in your browser
    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find the ID login field, where we will enter a false username or email
        login_elem = self.driver.find_element(By.ID, "login_field")

        # Entering an incorrect username or invalid email address
        login_elem.send_keys(username)

        # Find the field where we will enter the wrong password
        pass_elem = self.driver.find_element(By.ID, "password")
        
        # Enter the wrong password
        pass_elem.send_keys(password)

        # Find the “Sign in” button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Click (emulate a click) with the left mouse button
        btn_elem.click()
        
    # check if we are on the “Sign in to GitHub - GitHub” page
    def check_title(self, expected_title):
        return self.driver.title == expected_title
    