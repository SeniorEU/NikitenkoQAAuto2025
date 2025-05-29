from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    def __init__(self) -> None:
        # Initialize Chrome WebDriver using WebDriver Manager
        # This automatically installs and uses the correct driver version
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the specified URL
    def go_to(self, url):
        self.driver.get(url)

    # Close the current browser window (not the whole session)
    def close(self):
        self.driver.close()

        