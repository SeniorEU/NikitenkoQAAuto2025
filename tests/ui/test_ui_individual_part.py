import pytest
from modules.ui.page_objects.tracking_page import TrackingPage

# Test case for searching a not valid TTN number | Тестовий випадок для пошуку не дійсного номера ТТН
@pytest.mark.ui
def test_invalid_ttn_search_page_object():
    page = TrackingPage()
    page.go_to()
    page.search_ttn("12345678900") # не існуючий номер ТТН


    result = page.get_result_text()

    assert "not found | не знайдено" in result.lower() or "no information found | не знайдено інформацію" in result.lower()

    page.close()




