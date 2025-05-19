import pytest
from modules.common.database import NetflixDB

# Check for tables in the database
# Перевіряємо наявность таблиць у базі
@pytest.mark.database
def test_show_tables():
    db = NetflixDB()
    tables = db.get_all_tables()

    print("\033[94mTables:\033[0m \033[93m| Таблиці:\033[0m", tables)

    assert tables is not None
    assert len(tables) > 0


# Check the names of the columns in the ‘movie’ table
# Перевіряємо назви колонок у таблиці 'movie'
@pytest.mark.database
def test_movie_columns():
    db = NetflixDB()
    columns = db.get_table_columns('movie')

    print("\033[94mMovie columns:\033[0m \033[93m| Колонки таблиці 'movie':\033[0m", columns)

    assert columns
    assert len(columns) > 0


# Checking the most frequently used language in movies
# Перевіряємо найчастіше вживану мову серед фільмів
@pytest.mark.database
def test_popular_language():
    db = NetflixDB()
    result = db.get_most_common_locale()

    if result:
        lang, count = result[0]
        print(f"\033[94mTop language: {lang}, count: {count}\033[0m \033[93m| Найчастіша мова: {lang}, кількість: {count}\033[0m")
    else:
        print("\033[91mNo language data found\033[0m \033[93m| Дані по мові відсутні\033[0m")

    assert result
    assert len(result) == 1
    assert lang != ''
    assert count > 0

# Check the columns of the ‘tv_show’ table
# Перевіряємо колоноки таблиці 'tv_show'
@pytest.mark.database
def test_tv_show_columns():
    db = NetflixDB()
    columns = db.get_table_columns('tv_show')

    print("\033[94mTV show columns:\033[0m \033[93m| Колонки таблиці 'tv_show':\033[0m", columns)

    assert columns
    assert len(columns) > 0

# Check the columns of the ‘episode’ table
# Перевіряємо колоноки таблиці 'episode'
@pytest.mark.database
def test_episode_columns():
    db = NetflixDB()
    columns = db.get_table_columns('episode')

    print("\033[94mEpisode columns:\033[0m \033[93m| Колонки таблиці 'episode':\033[0m", columns)

    assert columns
    assert len(columns) > 0


# Let's find the longest movie
# Знайдемо найдовший фільм
@pytest.mark.database
def test_find_longest_movie():
    db = NetflixDB()
    result = db.get_longest_movie()

    print("\033[94mLongest movie:\033[0m \033[93m| Найдовший фільм:\033[0m", result)

    assert result
    assert isinstance(result[0][1], int)
    assert result[0][1] > 0


# Merge all titles from movies and TV shows
# Об'єднуємо назви фільмів і серіалів
@pytest.mark.database
def test_titles_union():
    db = NetflixDB()
    all_titles = db.get_all_titles_union()

    print("\033[94mSample titles:\033[0m \033[93m| Приклади назв:\033[0m", all_titles[:10])

    assert all_titles
    assert isinstance(all_titles[0][0], str)


# Here are the Top 10 longest films or shows
# Виводимо Топ-10 найдовших фільмів або шоу
@pytest.mark.database
def test_top_10_longest():
    db = NetflixDB()
    top10 = db.get_top_10_longest_movies()

    print("\033[94mTop 10 longest:\033[0m \033[93m| Топ-10 найдовших:\033[0m")
    for i, (title, runtime) in enumerate(top10, start=1):
        print(f"{i}) {title} — {runtime} min | хв")

    assert top10
    assert len(top10) == 10
    for entry in top10:
        assert entry[1] > 0


# Finding series with multiple seasons
# Знаходимо серіали з кількома сезонами
@pytest.mark.database
def test_tv_multiple_seasons():
    db = NetflixDB()
    shows = db.get_tv_shows_with_multiple_seasons()

    print("\033[94mShows with >1 season:\033[0m \033[93m| Серіалів з >1 сезоном:\033[0m", len(shows))

    assert shows is not None
    assert len(shows) >= 0


# Find out how many film titles have been duplicated
# Знаходимо скільки назв фільмів продубльовано
@pytest.mark.database
def test_duplicate_movies():
    db = NetflixDB()
    duplicates = db.count_duplicate_movie_titles()

    print("\033[94mDuplicate titles:\033[0m \033[93m| Повторювані назви фільмів:\033[0m", duplicates)

    assert duplicates >= 0
