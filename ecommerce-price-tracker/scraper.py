import requests
import pandas as pd
import time
import random
import logging
from bs4 import BeautifulSoup
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://books.toscrape.com/catalogue/"
CATEGORY_URL = "https://books.toscrape.com/catalogue/category/books/{}/index.html"
OUTPUT_FILE = Path(__file__).parent / "data.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; EcommercePriceTracker/1.0)",
}

RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def get_categories():
    logger.info("Fetching category list...")
    response = requests.get("https://books.toscrape.com/", headers=HEADERS, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    categories = {}
    for a in soup.select("ul.nav-list ul a"):
        name = a.text.strip()
        # Extract slug from href e.g. "catalogue/category/books/mystery_3/index.html"
        slug = a["href"].split("books/")[1].replace("/index.html", "")
        categories[name] = slug

    logger.info(f"Found {len(categories)} categories")
    return categories


def scrape_category(category_name, slug):
    books = []
    page = 1

    while True:
        # Build page URL — first page has different format than subsequent pages
        if page == 1:
            url = f"https://books.toscrape.com/catalogue/category/books/{slug}/index.html"
        else:
            url = f"https://books.toscrape.com/catalogue/category/books/{slug}/page-{page}.html"

        response = requests.get(url, headers=HEADERS, timeout=15)

        # 404 means no more pages
        if response.status_code == 404:
            break

        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.select("article.product_pod")

        if not articles:
            break

        for article in articles:
            title = article.select_one("h3 a")["title"]
            price = article.select_one("p.price_color").text.strip()
            rating_class = article.select_one("p.star-rating")["class"][1]
            rating = RATING_MAP.get(rating_class, 0)
            availability = article.select_one("p.availability").text.strip()
            relative_url = article.select_one("h3 a")["href"].replace("../../../", "")
            book_url = BASE_URL + relative_url

            books.append({
                "title":        title,
                "category":     category_name,
                "price_gbp":    float(price.replace("£", "").replace("Â", "").strip()),
                "rating":       rating,
                "availability": availability,
                "url":          book_url,
            })

        page += 1
        time.sleep(random.uniform(0.5, 1.5))

    return books


def run():
    logger.info("Pipeline starting...")
    all_books = []

    categories = get_categories()

    for i, (name, slug) in enumerate(categories.items(), 1):
        logger.info(f"[{i}/{len(categories)}] Scraping: {name}")
        books = scrape_category(name, slug)
        all_books.extend(books)
        logger.info(f"  -> {len(books)} books found (total so far: {len(all_books)})")
        time.sleep(random.uniform(1, 2))

    df = pd.DataFrame(all_books)
    df = df.drop_duplicates(subset=["url"]).reset_index(drop=True)

    # Add price band column for analysis
    df["price_band"] = pd.cut(
        df["price_gbp"],
        bins=[0, 10, 20, 35, 60],
        labels=["Budget (£0-10)", "Mid (£10-20)", "Upper-Mid (£20-35)", "Premium (£35+)"]
    )

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    logger.info(f"Saved {len(df)} records to {OUTPUT_FILE}")

    # Quick summary
    logger.info("---")
    logger.info(f"Total books      : {len(df)}")
    logger.info(f"Categories       : {df['category'].nunique()}")
    logger.info(f"Avg price        : £{df['price_gbp'].mean():.2f}")
    logger.info(f"Price range      : £{df['price_gbp'].min():.2f} - £{df['price_gbp'].max():.2f}")

    return df


if __name__ == "__main__":
    df = run()
    if not df.empty:
        print("\n-- Sample Output ---------------------------------")
        print(df[["title", "category", "price_gbp", "rating"]].head())
