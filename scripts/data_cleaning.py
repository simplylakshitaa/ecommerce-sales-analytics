import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_CLEANED = os.path.join(BASE_DIR, "data", "cleaned")
os.makedirs(DATA_CLEANED, exist_ok=True)


def clean_customers():
    print("\n--- Cleaning Customers ---")

    df = pd.read_csv(os.path.join(DATA_RAW, "olist_customers_dataset.csv"))
    print("Raw shape:", df.shape)
    df = df.drop_duplicates(subset="customer_id")
    df["customer_city"] = df["customer_city"].str.lower().str.strip()
    df["customer_state"] = df["customer_state"].str.lower().str.strip()
    df.to_csv(os.path.join(DATA_CLEANED, "customers_cleaned.csv"), index=False)
    print("Cleaned shape:", df.shape)

def clean_orders():
    print("\n--- Cleaning Orders ---")
    df = pd.read_csv(os.path.join(DATA_RAW, "olist_orders_dataset.csv"))
    print("Raw shape:", df.shape)
    df = df.dropna(subset=["order_id"])
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    df["order_status"] = df["order_status"].str.lower().str.strip()

    df.to_csv(os.path.join(DATA_CLEANED, "orders_cleaned.csv"), index=False)
    print("Cleaned shape:", df.shape)


def main():
    print("Starting data cleaning pipeline...")
    clean_customers()
    clean_orders()
    print("Data cleaning completed successfully.")


if __name__ == "__main__":
    main()
