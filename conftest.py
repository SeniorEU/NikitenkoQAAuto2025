import pytest
from modules.api.clients.github import GitHub
from modules.common.database import NetflixDB


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


@pytest.fixture(scope="module")
def netflix_db():
    db = NetflixDB()
    yield db
    db.close()

# Create a fixture for Rozetka with automatic closing 
from modules.ui.page_objects.rozetka_login_page import RozetkaLoginPage

@pytest.fixture
def rozetka_page():
    page = RozetkaLoginPage()
    yield page
    page.close()