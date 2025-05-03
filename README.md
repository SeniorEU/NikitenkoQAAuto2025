# GitHub API Tests
This project contains automated tests for verifying GitHub REST API using `pytest` and `requests`.

## 📦 Installation
1. Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. (Optional) Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Linux/Mac

3. Install dependencies:
pip install -r requirements.txt

> If `requirements.txt` is missing, install manually:
pip install pytest requests python-dotenv

---
## 🔐 GitHub Token Setup
1. Create a `.env` file in the project root.
2. Copy from `.env.example`.
3. Paste your personal GitHub token:

GITHUB_TOKEN=your_token_here

> Generate your token here: [GitHub → Developer Settings → Tokens](https://github.com/settings/tokens)

## 🚀 Run Tests
To run all tests with the `api` marker:
pytest -m api

To see extra output in the terminal:
pytest -m api -s

## 📁 Project Structure
├── modules/
│   └── api/clients/github.py
├── tests/
│   └── api/test_github_api.py
├── .env.example
├── .gitignore
├── pytest.ini
└── README.md


## 👤 Author
Ivan Nikitenko  
GitHub: [SeniorEU](https://github.com/SeniorEU)