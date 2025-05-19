from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Generating a class for the NYTimes home page
# Генеруємо клас для головної сторінки NYTimes
class NYTimesMainPage(BasePage):
    URL = "https://www.nytimes.com/section/business/economy"

    # Go to the NYTimes home page in the economics section
    # Перейти на головну сторінку NYTimes в розділі економіки
    def go_to(self):
        self.driver.get(NYTimesMainPage.URL)

    # Get all headlines from the NYTimes homepage with a 10-second pause
    # Отримати всі заголовки з головної сторінки NYTimes з паузою 10 секунд
    def get_all_headlines(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h2 | //h3"))
        )
        # Get a list of all headlines
        # отримуємо список всіх заголовків
        headlines = self.driver.find_elements(By.XPATH, "//h2 | //h3")

        # For each header, el takes its text content, removes whitespace, filters for empty lines, and returns a clean list of headers
        # Для кожного заголовка el бере його вміст тексту, прибирає пробіли, фільтрує порожні рядки і повертає чистий список заголовків
        return [el.text for el in headlines if el.text.strip() != ""]