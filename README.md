# 🕷️ Web Scraping Projects

A collection of Python web scraping and data analysis projects built for portfolio purposes.

---

## 📁 Projects

### 1. [Job Market Analysis](./job-market-analysis/)
Scrapes remote job listings for data roles from the RemoteOK API and analyzes market demand.

- **Source:** RemoteOK public API
- **Data:** ~100 job listings per run
- **Analysis:** Role demand, top skills, salary ranges, hiring companies

### 2. [E-Commerce Price Tracker](./ecommerce-price-tracker/)
Crawls all 1000 products from an e-commerce bookstore and analyzes pricing trends across categories.

- **Source:** Books to Scrape (books.toscrape.com)
- **Data:** 1,000 products across 20 categories
- **Analysis:** Price distribution, category breakdown, rating vs price, availability

---

## 🛠️ Tech Stack

- **Python** — core language
- **Requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing
- **Pandas** — data wrangling
- **Matplotlib / Seaborn** — visualizations
- **Jupyter Notebook** — analysis environment

---

## 🚀 Setup

All projects share a single virtual environment at the root level.

```bash
# Clone the repo
git clone https://github.com/yourusername/web-scraping-projects.git
cd web-scraping-projects

# Create and activate venv
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# Install dependencies for all projects
pip install -r job-market-analysis/requirements.txt
pip install -r ecommerce-price-tracker/requirements.txt
```

Then navigate into any project folder and run:

```bash
python scraper.py
jupyter notebook analysis.ipynb
```

---

## 📄 License

MIT License
