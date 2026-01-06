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


def main():
    print("Starting data cleaning pipeline...")
    clean_customers()
    print("Data cleaning completed successfully.")


if __name__ == "__main__":
    main()
