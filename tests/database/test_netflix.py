import pytest
from modules.common.database import NetflixDB

# Seeing which tables are present in the netflixdb.sqlite database
# Дивимося які таблиці присутні в базі netflixdb.sqlite 
@pytest.mark.database
def test_list_all_tables():
    db = NetflixDB()
    tables = db.get_all_tables()
    print("List of tables in the database/Список таблиць у базі:", tables)

    assert tables is not None
    assert len(tables) > 0

# Let's look at the column titles in the ‘Films’ table
# Дивимося на назви колонок у таблиці 'Films'
@pytest.mark.database
def test_movie_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('movie')
    print("\nColumns in the ‘movie’ table/Колонки в таблиці 'movie':", columns)

    assert columns is not None
    assert len(columns) > 0

# Looking for the most common language among films.
# Шукаємо найпоширнішу мову серед фільмів.
@pytest.mark.database
def test_most_common_locale():
    db = NetflixDB()
    result = db.get_most_common_locale()

    print("Looking for the most common language among films/Шукаємо найпоширнішу мову серед фільмів:", result)

    assert result is not None
    assert len(result) == 1
    assert result[0][0] != ''
    assert result[0][1] > 0

@pytest.mark.database
def test_tv_show_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('tv_show')
    print("\nColumns in the ‘tv_show’ table/Колонки в таблиці 'tv_show':", columns)

    assert columns is not None
    assert len(columns) > 0

@pytest.mark.database
def test_episode_table_columns():
    db = NetflixDB()
    columns = db.get_table_columns('episode')
    print("\nColumns in the ‘episode’ table/Колонки в таблиці 'episode':", columns)

    assert columns is not None
    assert len(columns) > 0