import pytest
from modules.ui.page_objects.tracking_page import TrackingPage

# Test case for searching a not valid TTN number
@pytest.mark.ui
def test_invalid_ttn_search_page_object():
    page = TrackingPage()
    page.go_to()
    fake_ttn = "12345678900" # non-existent TTN number
    page.search_ttn(fake_ttn)

    # Wait for the result text to appear
    result = page.get_result_text().lower()
    print(f"\033[94mResult text\033[0m {result}")
    # Check if the result contains the expected text
    expected_phrases = [
        "не знайдено",
        "не знайшли",
        "не знайдено інформацію",
        "не знайдено текст",
        "ми не знайшли посилку"
    ]
    # Assert that the result contains at least one of the expected phrases
    assert any(phrase in result for phrase in expected_phrases), f"\033[94m]The result text does not meet expectations\033[0m] {result}"


    page.close()

