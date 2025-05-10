from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generating a class for the NYTimes home page
# Генеруємо клас для головної сторінки NYTimes
class NYTimesMainPage(BasePage):
    URL = "https://www.nytimes.com/section/business/economy"

    def go_to(self):
        self.driver.get(NYTimesMainPage.URL)

    def get_all_headlines(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h2 | //h3"))
        )
        headlines = self.driver.find_elements(By.XPATH, "//h2 | //h3")
        return [el.text for el in headlines if el.text.strip() != ""]