from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Page object for the Nova Poshta tracking page | Об'єкт сторінки для сторінки відстеження Нової Пошти
# This class encapsulates the behavior of the tracking page | Цей клас інкапсулює поведінку сторінки відстеження
class TrackingPage(BasePage):
    URL = "https://tracking.novaposhta.ua/#/uk"

    def go_to(self):
        self.driver.get(TrackingPage.URL)

    def search_ttn(self, ttn_number):
        print(f"Open the field for entering the TTN | Відкриваємо поле для вводу ТТН...")
        ttn_input = self.driver.find_element(By.ID, "en")
        ttn_input.clear()  # Clear the field before entering | Очищуємо поле перед введенням
        print(f"Enter the TTN number | Вводимо номер ТТН: {ttn_number}")
        ttn_input.send_keys(ttn_number)

        search_button = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        print(f"Click the 'Search' button | Натискаємо кнопку 'Пошук'")
        search_button.click()

    def get_result_text(self):
        try:
            # чекаємо на текст результату в спеціальному класі
            error_block = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tracking-result-text"))
            )
            return error_block.text
        except TimeoutException:
            return "Text not found | Не знайдено текст"
