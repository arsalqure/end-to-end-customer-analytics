# scripts/etl_run.py
import os, logging, sqlite3, subprocess, sys, zipfile
from pathlib import Path
import pandas as pd

logging.basicConfig(level=logging.INFO)
DATA_DIR = Path('../data')
DATA_DIR.mkdir(exist_ok=True, parents=True)

# Note: This script expects kaggle CLI configured with API token.
KAGGLE_CMD = "kaggle datasets download -d psparks/instacart-market-basket-analysis -p {}".format(DATA_DIR)

def download_kaggle():
    try:
        logging.info("Downloading dataset from Kaggle (requires kaggle CLI and credentials)...")
        subprocess.run(KAGGLE_CMD, shell=True, check=True)
        logging.info("Download complete.")
    except subprocess.CalledProcessError as e:
        logging.error("Kaggle download failed: %s", e)
        raise

def extract_and_load_sqlite(db_path='../data/instacart.db'):
    try:
        zfiles = list(DATA_DIR.glob('*.zip'))
        if not zfiles:
            logging.warning("No zip file found in data/. Make sure you downloaded dataset.")
            return
        zfile = zfiles[0]
        with zipfile.ZipFile(zfile, 'r') as z:
            z.extractall(DATA_DIR)
        conn = sqlite3.connect(db_path)
        for fname in ['orders.csv','products.csv','order_products__prior.csv','aisles.csv','departments.csv']:
            fpath = DATA_DIR/fname
            if fpath.exists():
                logging.info("Loading %s to sqlite.", fname)
                df = pd.read_csv(fpath)
                df.to_sql(fname.replace('.csv',''), conn, if_exists='replace', index=False)
        conn.close()
        logging.info("Data loaded to sqlite at %s", db_path)
    except Exception as e:
        logging.exception("ETL failed: %s", e)
        raise

if __name__ == '__main__':
    try:
        download_kaggle()
        extract_and_load_sqlite()
        logging.info("ETL completed successfully.")
    except Exception as e:
        logging.error("ETL process terminated with error.")
        sys.exit(1)
