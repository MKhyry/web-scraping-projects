# 📊 Job Market Analysis

A Python web scraping project that collects remote job listings for data roles and analyzes market demand.

---

## 🛠️ Tech Stack

- **Python** — core language
- **Requests** — fetch data from the API
- **Pandas** — clean and structure the data
- **Matplotlib / Seaborn** — visualizations
- **Jupyter Notebook** — analysis environment

---

## 📁 Project Structure

```
job-market-analysis/
├── scraper.py        # Fetches, cleans, and saves job listings
├── data.csv          # Scraped dataset (150 rows)
├── analysis.ipynb    # EDA notebook with charts and insights
├── requirements.txt  # Project dependencies
└── README.md
```

---

## 📊 What It Analyzes

- Most in-demand job titles
- Top hiring companies
- Jobs by location
- Salary ranges by role
- Most requested skills (Python, SQL, Tableau, etc.)
- Posting trends over time

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/web-scraping-projects.git
cd web-scraping-projects/job-market-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python scraper.py

# 4. Open the notebook
jupyter notebook analysis.ipynb
```

---

## 📈 Sample Results

| Role | Listings |
|---|---|
| Data Engineer | 38 |
| Machine Learning Engineer | 32 |
| BI Developer | 31 |
| Data Scientist | 26 |
| Data Analyst | 23 |

**Top skills:** Python · SQL · Tableau · Docker · TensorFlow

---

## 📄 License

MIT License