# 📦 E-Commerce Price Tracker

A Python web scraping project that collects product listings from an e-commerce bookstore and analyzes pricing trends across categories.

---

## 🛠️ Tech Stack

- **Python** — core language
- **Requests** — HTTP requests
- **BeautifulSoup4** — HTML parsing
- **Pandas** — data cleaning and analysis
- **Matplotlib / Seaborn** — visualizations
- **Jupyter Notebook** — analysis environment

---

## 📁 Project Structure

```
ecommerce-price-tracker/
├── scraper.py        # Crawls all categories and saves product data
├── data.csv          # Scraped dataset (1000 rows)
├── analysis.ipynb    # EDA notebook with 7 charts
├── requirements.txt  # Project dependencies
└── README.md
```

---

## 📊 What It Analyzes

- Price distribution across all products
- Average and price range per category
- Budget vs mid vs premium product breakdown
- Rating vs price relationship
- Availability by price band
- Category × price band heatmap

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/web-scraping-projects.git
cd web-scraping-projects/ecommerce-price-tracker

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper (~2-3 mins)
python scraper.py

# 4. Open the notebook
jupyter notebook analysis.ipynb
```

---

## 📈 Sample Results

| Metric | Value |
|---|---|
| Total products | 1,000 |
| Categories | 20 |
| Average price | £29.97 |
| Price range | £1.13 — £59.97 |
| In stock | 86.8% |
| Most expensive category | Crime |
| Cheapest category | Mystery |

**Price band breakdown:**

| Band | Count |
|---|---|
| Budget (£0–10) | 157 |
| Mid (£10–20) | 187 |
| Upper-Mid (£20–35) | 253 |
| Premium (£35+) | 403 |

---

## 📄 License

MIT License
