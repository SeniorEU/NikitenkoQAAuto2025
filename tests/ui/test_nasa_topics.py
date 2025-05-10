import pytest
from modules.ui.page_objects.nasa_main_page import NasaMainPage

# Checked the number of articles on the NASA main page
# Перевірив кількість статей на головній сторінці NASA
@pytest.mark.ui
def test_nasa_topic_titles():
    keywords = ["climate", "moon", "mars"] # search for articles using these keywords | шукаємо статті за цими ключовими словами
    page = NasaMainPage()
    page.go_to()

    titles = page.get_all_article_titles()
    print(f"\033[93mTotal headlines found | Всього знайдено заголовків: {len(titles)}\033[0m")

    for keyword in keywords:
        matched = [t for t in titles if keyword.lower() in t.lower()]
        print(f"\033[92mArticles with | Статті з'{keyword}': {len(matched)}\033[0m")
        for i, title in enumerate(matched, start=1):
            print(f"\033[94mArticle title | Назва статті > {i}. {title}\033[0m")
        if matched:
            for i, title in enumerate(matched, start=1):
                print(f"\033[94mArticle title | Назва статті > {i}. {title}\033[0m")
        else:
            print(f"\033[93mNo articles found with keyword | За ключовим словом не знайдено статей'{keyword}'\033[0m")

    page.close()
