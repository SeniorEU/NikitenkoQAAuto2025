import pytest
from modules.common.database import NetflixDB

# Seeing which tables are present in the netflixdb.sqlite database
# Дивимося які таблиці присутні в базі netflixdb.sqlite 
@pytest.mark.database
def test_list_all_tables():
    db = NetflixDB()
    tables = db.get_all_tables()
    print("List of tables in the database|Список таблиць у базі:", tables)

    assert tables is not None
    assert len(tables) > 0

# Let's look at the column titles in the ‘Films’ table
# Дивимося на назви колонок у таблиці 'Films'
@pytest.mark.database
def test_movie_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('movie')
    print("\nColumns in the ‘movie’ table|Колонки в таблиці 'movie':", columns)

    assert columns is not None
    assert len(columns) > 0

# Looking for the most common language among films.
# Шукаємо найпоширнішу мову серед фільмів.
@pytest.mark.database
def test_most_common_locale():
    db = NetflixDB()
    result = db.get_most_common_locale()

    print("Looking for the most common language among films|Шукаємо найпоширнішу мову серед фільмів:", result)

    assert result is not None
    assert len(result) == 1
    assert result[0][0] != ''
    assert result[0][1] > 0

@pytest.mark.database
def test_tv_show_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('tv_show')
    print("\nColumns in the ‘tv_show’ table|Колонки в таблиці 'tv_show':", columns)

    assert columns is not None
    assert len(columns) > 0

@pytest.mark.database
def test_episode_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('episode')
    print("\nColumns in the ‘episode’ table|Колонки в таблиці 'episode':", columns)

    assert columns is not None
    assert len(columns) > 0

# Looking the longest film.
# Шукаємо найдовший фільм.
@pytest.mark.database
def test_longest_movie():
    db = NetflixDB()
    result = db.get_longest_movie()

    print("The longest film|Найдовший фільм:", result)

    assert result is not None
    assert len(result) == 1
    assert isinstance(result[0][1], int)
    assert result[0][1] > 0

# Movie and TV series titles (combined)
# Назви фільмів і серіалів (об'єднані)
@pytest.mark.database
def test_union_all_titles():
    db = NetflixDB()
    result = db.get_all_titles_union()

    print("Movie and TV series titles (combined)|Назви фільмів і серіалів (об'єднані):", result[:10])  

    assert result is not None
    assert len(result) > 0
    assert isinstance(result[0][0], str)

# Looking 10 for the longest film or show.
# Шукаємо 10 найдовшхй фільм або шоу.
@pytest.mark.database
def test_top_10_longest_movies():
    db = NetflixDB()
    result = db.get_top_10_longest_movies()

    print("10 for the longest film or show|10 найдовших фільмів або шоу:")
    for i, (title, runtime) in enumerate(result, start=1):
        print(f"{i}. {title} — {runtime} хв.")

    assert result is not None
    assert len(result) == 10
    for item in result:
        assert isinstance(item[1], int)
        assert item[1] > 0
    
# Output the number of television shows (tv_show) that have more than one season
# Виводимо кількість телевізійні шоу (tv_show) які мають більше одного сезону
@pytest.mark.database
def test_count_tv_shows_with_multiple_seasons():
    db = NetflixDB()
    result = db.get_tv_shows_with_multiple_seasons()

    total = len(result)
    print(f"Number of TV series with more than one season|Кількість серіалів, які мають більше одного сезону: {total}")

    assert result is not None
    assert total >= 0

# Шукаємо дублікати назв у таблиці movie (однакові значення title) і виводимо кількість
@pytest.mark.database
def test_count_duplicate_movie_titles():
    db = NetflixDB()
    count = db.count_duplicate_movie_titles()

    print(f"Number of duplicate film titles | Кількість дублюющихся назв фільмів: {count}")

    assert count >= 0