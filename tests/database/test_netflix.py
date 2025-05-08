import pytest
from modules.common.database import NetflixDB

# Seeing which tables are present in the netflixdb.sqlite database
# Дивимося які таблиці присутні в базі netflixdb.sqlite 
@pytest.mark.database
def test_list_all_tables():
    db = NetflixDB()
    tables = db.get_all_tables()
    print("Список таблиць у базі:", tables)

    assert tables is not None
    assert len(tables) > 0

