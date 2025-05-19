from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Search and display the number of articles on the website uk.wikipedia.org
# шукаємо і виводимо кількість статей на сайті uk.wikipedia.org
class WikipediaStatsPage(BasePage):
    URL = "https://uk.wikipedia.org/wiki/Спеціальна:Статистика"

    # Go to the Wikipedia statistics page | Перейти на сторінку статистики Вікіпедії
    def go_to(self):
        self.driver.get(WikipediaStatsPage.URL)

    # Get the number of articles on the Wikipedia website | Отримати кількість статей на сайті Вікіпедії
    # The function waits for the element with ID "mw-content-text" to be visible and then extracts the number of articles from the text
    # Функція чекає, поки елемент з ID "mw-content-text" стане видимим а потім витягує кількість статей з тексту
    def get_article_count(self):
        content = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "mw-content-text")) 
        )
        full_text = content.text
        
        # Extract the number of articles using a regular expression 
        # Витягти кількість статей за допомогою регулярного виразу
        import re
        match = re.search(r"\)\s*([0-9\u00a0\s]+)", full_text)
        if match:
            number_text = match.group(1).replace(" ", "").replace("\xa0", "")
            return int(number_text)
        
        # If the number of articles is not found, raise an exception
        # Якщо кількість статей не знайдено, викликати виняток
        raise Exception("\033[91m Could not find the number of articles in the text\033[0m | \033[93mНе вдалося знайти кількість статей у тексті\033[0m")
