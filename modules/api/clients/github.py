import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GitHub:
    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}', headers=self.headers)
        r.raise_for_status()
        return r.json()

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}, headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_emojis(self):
        r = requests.get("https://api.github.com/emojis", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_commits(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_followers(self, username):
        r = requests.get(f"https://api.github.com/users/{username}/followers", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_branches(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_rate_limit(self):
        r = requests.get("https://api.github.com/rate_limit", headers=self.headers)
        r.raise_for_status()
        return r.json()

    def get_authenticated_user(self):
        r = requests.get("https://api.github.com/user", headers=self.headers)
        r.raise_for_status()
        return r.json()
