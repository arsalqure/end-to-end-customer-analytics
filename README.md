# Instacart Flagship Data Analytics Project — Arsalan Ahmed

## Project overview
**Domain:** E-commerce / Grocery  
**Objective:** Reduce churn and increase repeat purchases by identifying high-value customers, building customer segments (RFM), and creating a purchase-propensity model.

## Dataset
Instacart Market Basket Analysis (Kaggle) — orders, order_products_prior/train, products, aisles, departments.

## Tools & Tech
- Python (pandas, numpy, scikit-learn, matplotlib, seaborn, plotly)
- SQL (Postgres / SQLite)
- Power BI / Tableau Public (dashboard)
- GitHub (repo)
- Kaggle CLI (data ingestion)

## Structure
```
/instacart-flagship-project/
├─ README.md
├─ /data/                    # small sample CSVs or pointers (raw files should NOT be committed)
├─ /notebooks/
│   ├─ 01_data_ingest_etl.ipynb
│   ├─ 02_eda_visuals.ipynb
│   ├─ 03_rfm_cohort_analysis.ipynb
│   ├─ 04_churn_modeling.ipynb
│   └─ 05_ab_test_simulation.ipynb
├─ /sql/
├─ /scripts/
├─ /docs/
├─ /dashboards/
└─ blog_post.md
```

## How to run
1. Install dependencies (create a `requirements.txt` if needed).
2. Use Kaggle API to download dataset: `kaggle datasets download -d psparks/instacart-market-basket-analysis -p data/`
3. Run `python scripts/etl_run.py` to load to SQLite.
4. Open notebooks in `/notebooks/` and run sequentially.

## Key findings (placeholder - run notebooks to compute concrete numbers)
- Top 10% customers often contribute ~30-40% of revenue.
- Customers with recency > 90 days show low repeat probability — candidates for win-back campaigns.
- Propensity modeling + CLV targeting recommended to maximize marketing ROI.

## Dashboard link
Add Tableau Public / Power BI Service link here after publishing.

## Contact
LinkedIn: https://www.linkedin.com/in/your-profile  • Email: your.email@example.com
