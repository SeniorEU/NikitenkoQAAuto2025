import pytest
from modules.ui.page_objects.wikipedia_main_page import WikipediaStatsPage

# Test case to check the number of articles on the Ukrainian Wikipedia website
@pytest.mark.ui
def test_uk_wikipedia_main_page_count():
    page = WikipediaStatsPage()
    page.go_to()

    # Get the number of articles on the Ukrainian Wikipedia website
    count = page.get_article_count()
    print(f"\033[93m Number of articles on the Ukrainian Wikipedia website: {count}\033[0m ")

    # Check that the number of articles is greater than 1 million
    assert count > 1_000_000
    page.close()