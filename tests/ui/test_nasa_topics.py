import pytest
from modules.ui.page_objects.nasa_main_page import NasaMainPage

# Check the number of articles on the NASA homepage
# Перевіряємо кількість статей на головній сторінці NASA
@pytest.mark.ui
def test_nasa_topic_titles():
    # Keywords we want to find in article titles
    # Ключові слова, які хочемо знайти в заголовках
    keywords = ["space", "moon", "mars", "earth", "nasa"]

    page = NasaMainPage()
    page.go_to()

    # Get all titles from the page
    # Отримуємо всі заголовки зі сторінки
    titles = page.get_all_article_titles()
    print(f"\033[94mTotal article titles found:\033[0m \033[93m| Всього знайдено заголовків:\033[0m {len(titles)}")

    # For each keyword — check how many matches
    # Для кожного ключового слова — перевіряємо кількість збігів
    for keyword in keywords:
        matched = [t for t in titles if keyword.lower() in t.lower()]
        print(f"\033[94mArticles containing '{keyword}':\033[0m \033[93m| Статті з '{keyword}':\033[0m {len(matched)}")

        if matched:
            for i, title in enumerate(matched, start=1):
                print(f"\033[94mTitle:\033[0m \033[93m| Назва:\033[0m {i}. {title}")
        else:
            print(f"\033[94mNo articles found with keyword '{keyword}'\033[0m \033[93m| За ключовим словом '{keyword}' не знайдено жодної статті\033[0m")

    page.close()

