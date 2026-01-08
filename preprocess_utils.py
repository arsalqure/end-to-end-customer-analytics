# scripts/preprocess_utils.py
import pandas as pd
import numpy as np

def basic_clean_str(df):
    df = df.copy()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    return df

def simulate_prices_if_missing(products_df, seed=42):
    products = products_df.copy()
    if 'price' not in products.columns:
        np.random.seed(seed)
        products['price'] = (np.random.exponential(30, products.shape[0]) + 5).round(2)
    return products
