import pytest
from modules.ui.page_objects.tracking_page import TrackingPage

@pytest.mark.ui
def test_invalid_ttn_search_page_object():
    page = TrackingPage()
    page.go_to()
    page.search_ttn("12345678900") # фейковий ТТН


    result = page.get_result_text()

    assert "не знайдено" in result.lower() or "не знайдено інформацію" in result.lower()

    page.close()




