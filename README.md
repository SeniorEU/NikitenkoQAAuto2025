# 🧪 QA Automation Final Project

This project is a collection of **UI** and **Database** automated tests created for the final assignment of the QA Automation course.

Tests are written using **Python**, **PyTest**, **Selenium WebDriver**, and **SQLite3**.

---

## 🌍 UI Tests

UI tests use Selenium to simulate user actions and verify functionality across popular websites:

| Site | Description |
|------|-------------|
| 🌐 [Wikipedia](https://uk.wikipedia.org/) | Check that Ukrainian Wikipedia has over 1 million articles |
| 💼 [GitHub](https://github.com/login) | Negative login tests with incorrect credentials |
| 📦 [Rozetka](https://rozetka.com.ua/) | Login form validation with fake credentials |
| 🚚 [Nova Poshta](https://novaposhta.ua/) | Invalid TTN search scenario |
| 📰 [NYTimes](https://www.nytimes.com/) | Count articles about economy |
| 🚀 [NASA](https://www.nasa.gov/) | Find article titles related to space topics |

---

## 🗄️ Database Tests

Database tests work with **SQLite** databases (e.g., Netflix clone) to verify structure and contents:

| Feature | Description |
|--------|-------------|
| 🔎 Tables & Columns | Check for presence of expected tables/columns |
| 🧍 User Data | Verify user addresses and data structure |
| 🍿 NetflixDB | Validate movie/TV show metadata, duplicates, longest titles |
| 📦 Product CRUD | Insert, update, and delete products |
| 🧾 Orders | Check detailed order data (joins & structure) |

---

## 📁 Project Structure

```
tests/
├── ui/
│   ├── test_ui.py
│   ├── test_ui_page_object.py
│   ├── test_rozetka_login.py
│   ├── test_ui_individual_part.py
│   ├── test_wikipedia_article_count.py
│   ├── test_nytimes_economy_articles.py
│   └── test_nasa_topics.py
├── database/
│   ├── test_database.py
│   └── test_netflix.py
modules/
├── ui/page_objects/
│   └── *.py (Page Object classes)
├── common/
│   └── database.py, netflix.py
```

---

## ▶️ How to Run Tests

1. Clone the repository:
```bash
git clone https://github.com/your-username/qa-final-project.git
cd qa-final-project
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
pytest -m ui
```

5. Run only database tests:
```bash
pytest -m database
```

---

## 👨‍💻 Author

**Ivan Nikitenko**  
Student of QA Automation Course  
GitHub: [SeniorEU](https://github.com/SeniorEU)

---

_Thank you for reviewing my course project!_