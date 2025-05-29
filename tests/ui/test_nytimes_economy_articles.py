import pytest
from modules.ui.page_objects.nytimes_main_page import NYTimesMainPage

# Check the number of economic articles on the NYTimes homepage
@pytest.mark.ui
def test_economy_news_count():
    # Keywords we want to search in article titles
    keywords = ['economy', 'economic', 'inflation', 'market']

    page = NYTimesMainPage()
    page.go_to()

    # Get all headlines from the main page
    headlines = page.get_all_headlines()

    # Filter only economic-related headlines
    economy_titles = [h for h in headlines if any(k.lower() in h.lower() for k in keywords)]

    print(f"\033[94mTotal headlines:\033[0m {len(headlines)}\033[0m")
    print(f"\033[94mEconomic-related headlines:\033[0m {len(economy_titles)}\033[0m")

    # If there are any economic headlines — print them
    if len(economy_titles) > 0:
        for i, title in enumerate(economy_titles, start=1):
            print(f"\033[94mTitle:\033[0m {i}. {title}\033[0m")
    else:
        print(f"\033[94mNo economy-related articles found\033[0m ")
        

    page.close()
