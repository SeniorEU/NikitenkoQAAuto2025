import pytest
import sqlite3
from modules.api.clients.github import GitHub 



class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Ivan'
        self.second_name = 'Nikitenko'
    
    def remove(self):
        self.name = ''
        self.second_name = ''
    
@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api

# Create a NetflixDB class for testing and pass it to the test function
# Створюю клас NetflixDB для тестування і передаю його тестовій функції
class NetflixDB:
    def __init__(self, db_path='netflixdb.sqlite'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

@pytest.fixture(scope="module")
def netflix_db():
    db = NetflixDB()
    yield db
    db.close()