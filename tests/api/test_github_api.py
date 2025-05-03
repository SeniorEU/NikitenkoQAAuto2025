import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
        r = github_api.get_user('butenkosergii')
        assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emojis_contains_smile(github_api): # перевіряємо чи існують емодзі взагалі
    emojis = github_api.get_emojis()
    assert 'smile' in emojis

@pytest.mark.api
def test_total_emojis_count_is_large(github_api): # перевіряємо що емодзі більше 1000
    emojis = github_api.get_emojis()
    assert len(emojis) > 1000

@pytest.mark.api
def test_all_emoji_keys_are_strings(github_api): # перевіряємо що всі ключі в словнику емодзі це значення рядкового типу (str)
    emojis = github_api.get_emojis()
    assert all(isinstance(key, str) for key in emojis.keys())

@pytest.mark.api
def test_all_emojis_urls_are_png(github_api): # Перевіряємо, що всі значення емодзі (а саме в URL) мають в назві .png
    emojis = github_api.get_emojis()
    assert all(url.split('?')[0].endswith('.png') for url in emojis.values())

@pytest.mark.api
def test_commits_returned_repo(github_api): # перевіряємо що коміти повертаються з репозиторію 
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert isinstance(commits, list)
    assert len(commits) > 0

@pytest.mark.api
def test_commit_objects_have_commit_key(github_api): # перевіряємо що в комітах є ключ commit
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert 'commit' in commits[0]

@pytest.mark.api
def test_commit_has_author_info(github_api): # перевіряємо що в комітах є автор
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert 'author' in commits[0]['commit']
    assert 'name' in commits[0]['commit']['author']

@pytest.mark.api 
def test_user_has_followers(github_api): # перевіряємо що у користувача 'defunkt' є підписники
    followers = github_api.get_followers('defunkt')
    assert isinstance(followers, list)
    assert len(followers) > 0

@pytest.mark.api
def test_each_follower_has_login(github_api): # перевіряємо що перший підписник 'defunkt' має нікнейм (login)
    followers = github_api.get_followers('defunkt')
    assert 'login' in followers[0]

@pytest.mark.api
def test_repo_has_branches(github_api): # перевіряє чи є гілки в репозиторії
    branches = github_api.get_branches('octocat', 'Hello-World')
    assert isinstance(branches, list)
    assert len(branches) > 0

@pytest.mark.api
def test_branch_has_name_and_sha(github_api): # отримуємо всі гілки репозиторію і перевіряємо що має правильну структуру у вдповіді
    branches = github_api.get_branches('octocat', 'Hello-World')
    first_branch = branches[0]
    assert 'name' in first_branch
    assert 'commit' in first_branch
    assert 'sha' in first_branch['commit']

@pytest.mark.api
def test_rate_limit_structure(github_api):  # для початку перевіряємо, що відповідь має ключ 'rate' з інформацією про ліміт
    r = github_api.get_rate_limit()
    assert 'rate' in r
    assert 'remaining' in r['rate']

@pytest.mark.api
def test_rate_limit_remaining_positive(github_api):  # перевіряємо, скільки запитів у мене ще залишилось до досягнення ліміту
    r = github_api.get_rate_limit()
    remaining = r['rate']['remaining']
    assert isinstance(remaining, int)
    assert remaining > 0  # при досягнені ліміту може бути 0, якщо перевищено ліміт в 60 запитів за годину