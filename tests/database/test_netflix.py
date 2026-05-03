import pytest
from modules.common.database import NetflixDB

@pytest.mark.database
def test_show_tables():
    db = NetflixDB()
    tables = db.get_all_tables()
    db.close()

    print("\033[94mTables:\033[0m", tables)

    assert tables is not None
    assert len(tables) > 0


@pytest.mark.database
def test_movie_columns():
    db = NetflixDB()
    columns = db.get_table_columns('movie')
    db.close()

    print("\033[94mMovie columns:\033[0m", columns)

    assert columns
    assert len(columns) > 0


@pytest.mark.database
def test_popular_language():
    db = NetflixDB()
    result = db.get_most_common_locale()
    db.close()

    if result:
        lang, count = result[0]
        print(f"\033[94mTop language: {lang}, count: {count}\033[0m")
    else:
        print("\033[91mNo language data found\033[0m")

    assert result
    assert len(result) == 1
    assert lang != ''
    assert count > 0


@pytest.mark.database
def test_tv_show_columns():
    db = NetflixDB()
    columns = db.get_table_columns('tv_show')
    db.close()

    print("\033[94mTV show columns:\033[0m", columns)

    assert columns
    assert len(columns) > 0


@pytest.mark.database
def test_episode_columns():
    db = NetflixDB()
    columns = db.get_table_columns('episode')
    db.close()

    print("\033[94mEpisode columns:\033[0m", columns)

    assert columns
    assert len(columns) > 0


@pytest.mark.database
def test_find_longest_movie():
    db = NetflixDB()
    result = db.get_longest_movie()
    db.close()

    print("\033[94mLongest movie:\033[0m", result)

    assert result
    assert isinstance(result[0][1], int)
    assert result[0][1] > 0


@pytest.mark.database
def test_titles_union():
    db = NetflixDB()
    all_titles = db.get_all_titles_union()
    db.close()

    print("\033[94mSample titles:\033[0m", all_titles[:10])

    assert all_titles
    assert isinstance(all_titles[0][0], str)


@pytest.mark.database
def test_top_10_longest():
    db = NetflixDB()
    top10 = db.get_top_10_longest_movies()
    db.close()

    print("\033[94mTop 10 longest:\033[0m")
    for i, (title, runtime) in enumerate(top10, start=1):
        print(f"{i}) {title} — {runtime} min")

    assert top10
    assert len(top10) == 10
    for entry in top10:
        assert entry[1] > 0


@pytest.mark.database
def test_tv_multiple_seasons():
    db = NetflixDB()
    shows = db.get_tv_shows_with_multiple_seasons()
    db.close()

    print("\033[94mShows with >1 season:\033[0m", len(shows))

    assert shows is not None
    assert len(shows) >= 0


@pytest.mark.database
def test_duplicate_movies():
    db = NetflixDB()
    duplicates = db.count_duplicate_movie_titles()
    db.close()

    print("\033[94mDuplicate titles:\033[0m", duplicates)

    assert duplicates >= 0
