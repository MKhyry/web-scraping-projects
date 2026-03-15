import requests
import pandas as pd
import time
import random
import logging
from datetime import datetime
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

API_URL = "https://remoteok.com/api"
OUTPUT_FILE = Path(__file__).parent / "data.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; JobMarketBot/1.0)",
    "Accept": "application/json",
}

TARGET_ROLES = [
    "data", "data analyst", "data scientist", "data engineer",
    "machine learning", "ml engineer", "analytics engineer",
    "business intelligence", "bi developer", "bi analyst",
    "deep learning", "nlp engineer", "artificial intelligence",
    "databricks", "snowflake", "dbt",
]


def fetch_jobs():
    logger.info(f"Fetching jobs from {API_URL}")
    response = requests.get(API_URL, headers=HEADERS, timeout=15)
    response.raise_for_status()
    data = response.json()
    jobs = [item for item in data if isinstance(item, dict) and "position" in item]
    logger.info(f"Fetched {len(jobs)} total listings")
    return jobs


def filter_jobs(jobs):
    roles_lower = [r.lower() for r in TARGET_ROLES]
    relevant = []
    for job in jobs:
        title = job.get("position", "").lower()
        tags = " ".join(job.get("tags", [])).lower()
        if any(role in title or role in tags for role in roles_lower):
            relevant.append(job)
    logger.info(f"Filtered to {len(relevant)} data-related listings")
    return relevant


def extract_fields(jobs):
    records = []
    for job in jobs:
        salary_min = job.get("salary_min")
        salary_max = job.get("salary_max")

        if salary_min and salary_max:
            salary = f"${int(salary_min):,} - ${int(salary_max):,}"
        elif salary_min:
            salary = f"From ${int(salary_min):,}"
        elif salary_max:
            salary = f"Up to ${int(salary_max):,}"
        else:
            salary = "Not specified"

        tags = job.get("tags", [])
        skills = ", ".join(tags) if tags else "Not specified"

        try:
            posting_date = datetime.fromisoformat(job.get("date", "")).strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            posting_date = "Unknown"

        records.append({
            "job_title":    job.get("position", "Unknown").strip(),
            "company":      job.get("company", "Unknown").strip(),
            "location":     job.get("location", "Remote").strip() or "Remote",
            "salary":       salary,
            "skills":       skills,
            "posting_date": posting_date,
            "job_link":     job.get("url", "").strip(),
        })

    return records


def clean_df(df):
    df = df.drop_duplicates(subset=["job_link"], keep="first")
    df["company"] = df["company"].str.title()
    str_cols = df.select_dtypes(include="str").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())
    df.replace("", "Not specified", inplace=True)
    df = df.sort_values("posting_date", ascending=False).reset_index(drop=True)
    logger.info(f"Final record count: {len(df)}")
    return df


def run():
    logger.info("Pipeline starting...")

    jobs = fetch_jobs()

    time.sleep(random.uniform(2, 4))

    jobs = filter_jobs(jobs)
    if not jobs:
        logger.warning("No relevant jobs found.")
        return pd.DataFrame()

    records = extract_fields(jobs)
    df = pd.DataFrame(records)
    df = clean_df(df)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    logger.info(f"Saved {len(df)} records to {OUTPUT_FILE}")

    return df


if __name__ == "__main__":
    df = run()
    if not df.empty:
        print("\n── Sample Output ───────────────────────────────────")
        print(df[["job_title", "company", "location", "salary"]].head())