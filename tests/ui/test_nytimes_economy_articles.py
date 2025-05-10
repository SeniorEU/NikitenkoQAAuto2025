import pytest
from modules.ui.page_objects.nytimes_main_page import NYTimesMainPage

# Checked the number of economic articles on the NYTimes main page
# Перевірив кількість економічних статей на головній сторінці NYTimes
@pytest.mark.ui
def test_economy_news_count():
    keywords = ['economy', 'economic', 'inflation', 'market']
    page = NYTimesMainPage()
    page.go_to()

    headlines = page.get_all_headlines()
    econ_headlines = [h for h in headlines if any(k.lower() in h.lower() for k in keywords)]

    print(f"\033[93m Total headlines | Заголовків всього: {len(headlines)}\033[0m")
    print(f"\033[92m Economic headlines | Економічні заголовки: {len(econ_headlines)}\033[0m")
    
    for i, title in enumerate(econ_headlines, start=1):
        print(f"\033[94mArticle title | Назва статті > {i}. {title}\033[0m")

    page.close()

