from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage
import time

class NasaMainPage(BasePage):
    URL = "https://www.nasa.gov/"

    def go_to(self):
        self.driver.get(NasaMainPage.URL)

    def get_all_article_titles(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3, h2"))
        )
        time.sleep(2)
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h3, h2")
        return [el.text for el in elements if el.text.strip()]
