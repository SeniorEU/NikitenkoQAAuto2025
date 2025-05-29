import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # Load the GitHub token from the .env file

# GitHub API interaction class
class GitHub:
    def __init__(self): # get a token
        # Retrieve GitHub token from environment and set headers
        token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {token}"} if token else {}

    # User information
    def get_user(self, username):
         # Send GET request to fetch user data by username
        r = requests.get(f'https://api.github.com/users/{username}', headers=self.headers)
        body = r.json()

        return body 
    
    # Repository search
    def search_repo(self, name):
        # Search repositories by name using query parameters
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}, headers=self.headers)
        body = r.json()

        return body
    # Emojis
    def get_emojis(self): 
        # Get a dictionary of all available emojis from GitHub
        r = requests.get("https://api.github.com/emojis", headers=self.headers)  
        body = r.json()
        return body
    
    # Commits
    def get_commits(self, owner, repo):
        # Get a list of commits from a specific repository
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits", headers=self.headers)
        body = r.json()
        return body
    
    # Followers
    def get_followers(self, username):
        # make a GET request that returns a list of subscribers
        r = requests.get(f"https://api.github.com/users/{username}/followers", headers=self.headers)
        body = r.json()
        return body
    
    # Branches
    def get_branches(self, owner, repo):
        # make a GET request that returns repository branches
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches", headers=self.headers)
        body = r.json()
        return body
    
    # Rate limit
    def get_rate_limit(self):
        # check how many API requests I can still make 
        r = requests.get(f"https://api.github.com/rate_limit", headers=self.headers)
        body = r.json()
        return body
    
    # Authenticated user
    def get_authenticated_user(self):
        # check how many requests to the API I can still make # check the connection of the token via a GET request and slightly change the structure of the method
        url = "https://api.github.com/user"
        r = requests.get(url, headers=self.headers)
        return r.json()







    

