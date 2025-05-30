# QA Automation Final Project

This project is a collection of **UI** and **Database** and **API** automated tests created for the final assignment of the QA Automation course.

Tests are written using **Python**, **PyTest**, **Selenium WebDriver**, and **SQLite3**.

---

## UI Tests

UI tests use Selenium to simulate user actions and verify functionality across popular websites:

| Site | Description |
|------|-------------|
| [Wikipedia](https://uk.wikipedia.org/) | Check that Ukrainian Wikipedia has over 1 million articles |
| [GitHub](https://github.com/login) | Negative login tests with incorrect credentials |
| [Rozetka](https://rozetka.com.ua/) | Login form validation with fake credentials |
| [Nova Poshta](https://novaposhta.ua/) | Invalid TTN search scenario |
| [NYTimes](https://www.nytimes.com/) | Count articles about economy |
| [NASA](https://www.nasa.gov/) | Find article titles related to space topics |

---

## Database Tests

Database tests work with **SQLite** databases (e.g., Netflix clone) to verify structure and contents:

| Feature | Description |
|--------|-------------|
| Tables & Columns | Check for presence of expected tables/columns |
| User Data | Verify user addresses and data structure |
| NetflixDB | Validate movie/TV show metadata, duplicates, longest titles |
| Product CRUD | Insert, update, and delete products |
| Orders | Check detailed order data (joins & structure) |

---

## API Tests

The API tests are located in the following files:

| Feature | Description |
|--------|-------------|
| https://api.github.com/zen | Returns a Zen phrase — used to check server availability |
| https://api.github.com/users/<username> | Returns user data — validate response fields and status codes |
| https://httpbin.org/anything | Mock server — used for structured request/response validation |

---

## File .gitattributes

This file was added to the repository to configure Git’s behavior for file handling, specifically:

normalizing line endings (`text=auto`) to ensure cross-platform compatibility between Windows and Unix systems.

This helps avoid issues when developers work on the project from different operating systems.

---

## How to Run Tests

1. Clone the repository:
```bash
git clone https://github.com/SeniorEU/NikitenkoQAAuto2025.git
cd NikitenkoQAAuto2025
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run all tests:
```bash
pytest -v
```

4. Run only UI tests:
```bash
pytest -s -m ui
```

5. Run only database tests:
```bash
pytest -s -m database
```
6. Run only api tests:
```bash
pytest -s -m api
```
---

## Project Structure

```
C:.
|
+---modules
|   +---api
|   |   \---clients
|   |       |   github.py
|   |
|   +---common
|   |   |   database.py
|   |
|   \---ui
|       \---page_objects
|           |   base_page.py
|           |   nasa_main_page.py
|           |   nytimes_main_page.py
|           |   rozetka_login_page.py
|           |   sign_in_page.py
|           |   tracking_page.py
|           |   wikipedia_main_page.py          
+---tests
|   +---api
|   |   |   test_api.py
|   |   |   test_fixtures.py
|   |   |   test_github_api.py
|   |   |   test_http.py
|   |
|   +---database
|   |   |   test_database.py
|   |   |   test_netflix.py
|   |
|   +---ui
|   |   |   test_nasa_topics.py
|   |   |   test_nytimes_economy_articles.py
|   |   |   test_rozetka_login.py
|   |   |   test_ui.py
|   |   |   test_ui_individual_part.py
|   |   |   test_ui_page_object.py
|   |   |   test_wikipedia_article_count.py
```

---
## Author

**Ivan Nikitenko**  
Student of QA Automation Course  
GitHub: [SeniorEU](https://github.com/SeniorEU)

---
_Thank you for reviewing my course project!_