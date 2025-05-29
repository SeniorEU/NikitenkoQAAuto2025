from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage
import time

# Generating a class for the NASA home page
class NasaMainPage(BasePage):
    URL = "https://www.nasa.gov/"

    # Navigate the browser to the NASA homepage
    def go_to(self):
        self.driver.get(NasaMainPage.URL)

    # Wait until all article titles (h2 and h3 tags) are loaded on the page
    def get_all_article_titles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3, h2"))
        )
        # Find all h3 and h2 elements after they are visible and ready
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h3, h2")
        
        # Return the list of non-empty text values from those elements
        return [el.text for el in elements if el.text.strip()]
    
    
