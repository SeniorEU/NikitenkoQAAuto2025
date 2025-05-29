import pytest

# Check if user defunkt exists
@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

# Check if non-existent user returns 'Not Found'
@pytest.mark.api
def test_user_not_exists(github_api):
        r = github_api.get_user('butenkosergii')
        assert r['message'] == 'Not Found'

# Check if repo become-qa-auto can be found
@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

# Check that fake repo cannot be found
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# Search for repos using a single character
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# check whether emojis exist at all
@pytest.mark.api
def test_emojis_contains_smile(github_api):
    emojis = github_api.get_emojis()
    assert 'smile' in emojis

# Check that emojis list has more than 1000 items
@pytest.mark.api
def test_total_emojis_count_is_large(github_api):
    emojis = github_api.get_emojis()
    assert len(emojis) > 1000

# check that all keys in the emoji dictionary are string values (str)
@pytest.mark.api
def test_all_emoji_keys_are_strings(github_api):
    emojis = github_api.get_emojis()
    assert all(isinstance(key, str) for key in emojis.keys())

# Check that all emoji URLs end with .png
@pytest.mark.api
def test_all_emojis_urls_are_png(github_api): 
    emojis = github_api.get_emojis()
    assert all(url.split('?')[0].endswith('.png') for url in emojis.values())

# check that the commits are returned from the repository 
@pytest.mark.api
def test_commits_returned_repo(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert isinstance(commits, list)
    assert len(commits) > 0

# check that there is a commit key in the commits
@pytest.mark.api
def test_commit_objects_have_commit_key(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert 'commit' in commits[0]

# check that the committees have an author
@pytest.mark.api
def test_commit_has_author_info(github_api):
    commits = github_api.get_commits('octocat', 'Hello-World')
    assert 'author' in commits[0]['commit']
    assert 'name' in commits[0]['commit']['author']

# check that the user “defunkt” has subscribers
@pytest.mark.api 
def test_user_has_followers(github_api): 
    followers = github_api.get_followers('defunkt')
    assert isinstance(followers, list)
    assert len(followers) > 0

# check that the first subscriber “defunkt” has a nickname (login)
@pytest.mark.api
def test_each_follower_has_login(github_api):
    followers = github_api.get_followers('defunkt')
    assert 'login' in followers[0]

# checks if there are branches in the repository
@pytest.mark.api
def test_repo_has_branches(github_api): 
    branches = github_api.get_branches('octocat', 'Hello-World')
    assert isinstance(branches, list)
    assert len(branches) > 0

# Check structure of repo branch (name, commit, sha)
@pytest.mark.api
def test_branch_has_name_and_sha(github_api):
    branches = github_api.get_branches('octocat', 'Hello-World')
    first_branch = branches[0]
    assert 'name' in first_branch
    assert 'commit' in first_branch
    assert 'sha' in first_branch['commit']

# Check structure of rate limit response
@pytest.mark.api
def test_rate_limit_structure(github_api):
    r = github_api.get_rate_limit()
    assert 'rate' in r
    assert 'remaining' in r['rate']

# Ensure remaining rate limit is positive
@pytest.mark.api
def test_rate_limit_remaining_positive(github_api):
    r = github_api.get_rate_limit()
    remaining = r['rate']['remaining']
    assert isinstance(remaining, int)
    assert remaining > 0 

# Ensure token is authenticated (check logged-in user)
@pytest.mark.api
def test_token_is_connected(github_api):
    user = github_api.get_authenticated_user()
    print("===> Authenticated user info:", user) # ← I want to see information in the console
    assert 'login' in user
    assert user['login'] == 'SeniorEU'