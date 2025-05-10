import pytest
from modules.ui.page_objects.wikipedia_main_page import WikipediaStatsPage

# Test for the number of articles on the Wikipedia main page
# Тест на кількість статей на головній сторінці Вікіпедії
@pytest.mark.ui
def test_uk_wikipedia_main_page_count():
    page = WikipediaStatsPage()
    page.go_to()

    count = page.get_article_count()
    print(f"\033[93m Number of articles on the Ukrainian Wikipedia website\033[0m | \033[94mКількість статей на сайті української Вікіпедії: {count}\033[0m")

    assert count > 1_000_000 # Check that the number of articles is greater than 1 million | Перевіряємо, що кількість статей більше 1 мільйона

    page.close()
