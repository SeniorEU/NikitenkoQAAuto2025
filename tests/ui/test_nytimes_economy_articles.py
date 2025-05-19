import pytest
from modules.ui.page_objects.nytimes_main_page import NYTimesMainPage

# Check the number of economic articles on the NYTimes homepage
# Перевіряємо кількість економічних статей на головній сторінці NYTimes
@pytest.mark.ui
def test_economy_news_count():
    # Keywords we want to search in article titles
    # Ключові слова для пошуку в заголовках
    keywords = ['economy', 'economic', 'inflation', 'market']

    page = NYTimesMainPage()
    page.go_to()

    # Get all headlines from the main page
    # Отримуємо всі заголовки з головної сторінки
    headlines = page.get_all_headlines()

    # Filter only economic-related headlines
    # Фільтруємо заголовки, пов’язані з економікою
    economy_titles = [h for h in headlines if any(k.lower() in h.lower() for k in keywords)]

    print(f"\033[94mTotal headlines:\033[0m \033[93m| Заголовків всього: {len(headlines)}\033[0m")
    print(f"\033[94mEconomic-related headlines:\033[0m \033[93m| Економічні заголовки: {len(economy_titles)}\033[0m")

    # If there are any economic headlines — print them
    # Якщо є економічні заголовки — виводимо їх
    if len(economy_titles) > 0:
        for i, title in enumerate(economy_titles, start=1):
            print(f"\033[94mTitle:\033[0m \033[93m| Назва: {i}. {title}\033[0m")
    else:
        print(f"\033[94mNo economy-related articles found\033[0m \033[93m| Економічні статті не знайдено\033[0m")

    page.close()
