import pytest
from modules.ui.page_objects.tracking_page import TrackingPage

# Test case for searching a not valid TTN number | Тестовий випадок для пошуку не дійсного номера ТТН
@pytest.mark.ui
def test_invalid_ttn_search_page_object():
    page = TrackingPage()
    page.go_to()
    fake_ttn = "12345678900" # non-existent TTN number | не існуючий номер ТТН
    page.search_ttn(fake_ttn)

    # Wait for the result text to appear | Очікуємо, поки з'явиться текст результату
    result = page.get_result_text().lower()
    print(f"\033[94mResult text\033[0m | \033[93mРезультат:\033[0m {result}")
    # Check if the result contains the expected text | Перевіряємо, чи містить результат очікуваний текст
    expected_phrases = [
        "не знайдено",
        "не знайшли",
        "не знайдено інформацію",
        "не знайдено текст",
        "ми не знайшли посилку"
    ]
    # Assert that the result contains at least one of the expected phrases | Перевіряємо, що результат містить хоча б одну з очікуваних фраз
    assert any(phrase in result for phrase in expected_phrases), f"\033[94m]The result text does not meet expectations\033[0m] | \033[93m]Текст результату не відповідає очікуванням:\033[0m] {result}"

    page.close()

