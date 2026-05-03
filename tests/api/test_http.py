import pytest
import requests

# Checking that the /zen endpoint returns text
@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f"Response is: {r.text}")

# Checking that the user ‘defunkt’ has the correct name and reply title
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert r.headers['Server'] == 'github.com'

# Checking that a request to a non-existent user gives a 404
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    
    assert r.status_code == 404



