import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Завантажуємо токен ключ з .env файл

class GitHub:
    def __init__(self): # отримуємо токен
        token = os.getenv("GITHUB_TOKEN")
        self.headers = {"Authorization": f"token {token}"} if token else {}

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}', headers=self.headers)
        body = r.json()

        return body 
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}, headers=self.headers)
        body = r.json()

        return body
    
    def get_emojis(self): # робимо GET-запит який повертає словник з emojis
        r = requests.get("https://api.github.com/emojis", headers=self.headers)  
        body = r.json()
        return body
    
    def get_commits(self, owner, repo): # робимо GET-запит який повертає коміти репозиторію
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits", headers=self.headers)
        body = r.json()
        return body
    
    def get_followers(self, username): # робимо GET-запит який повертає список підписників
        r = requests.get(f"https://api.github.com/users/{username}/followers", headers=self.headers)
        body = r.json()
        return body
    
    def get_branches(self, owner, repo): # робимо GET-запит який повертає гілки репозиторію
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches", headers=self.headers)
        body = r.json()
        return body
    
    def get_rate_limit(self): # перевіряємо скільки запитів до API я ще можу зробити
        r = requests.get(f"https://api.github.com/rate_limit", headers=self.headers)
        body = r.json()
        return body
    
    def get_authenticated_user(self): # перевіряємо підключення токена через GET-запит і трохи міняємо структуру написання методу
        url = "https://api.github.com/user"
        r = requests.get(url, headers=self.headers)
        return r.json()







    

