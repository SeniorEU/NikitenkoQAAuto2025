from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Search and display the number of articles on the website uk.wikipedia.org
# шукаємо і виводимо кількість статей на сайті uk.wikipedia.org
class WikipediaStatsPage(BasePage):
    URL = "https://uk.wikipedia.org/wiki/Спеціальна:Статистика"

    def go_to(self):
        self.driver.get(WikipediaStatsPage.URL)

    def get_article_count(self):
        content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mw-content-text"))
        )
        full_text = content.text
        
        import re
        match = re.search(r"\)\s*([0-9\u00a0\s]+)", full_text)
        if match:
            number_text = match.group(1).replace(" ", "").replace("\xa0", "")
            return int(number_text)

        raise Exception("\033[91m Could not find the number of articles in the text | Не вдалося знайти кількість статей у тексті\033[0m")
