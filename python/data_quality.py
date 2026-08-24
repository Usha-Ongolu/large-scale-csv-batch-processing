import pandas as pd


INPUT_FILE = "../data/sample_sales.csv"


def run_quality_checks(file_path):

    df = pd.read_csv(file_path)

    print("DATA QUALITY REPORT")
    print("====================")

    print(f"Total records: {len(df)}")

    print(
        f"Duplicate orders: "
        f"{df['order_id'].duplicated().sum()}"
    )

    print(
        f"Missing order IDs: "
        f"{df['order_id'].isna().sum()}"
    )

    print(
        f"Invalid quantities: "
        f"{(df['quantity'] <= 0).sum()}"
    )

    print(
        f"Invalid prices: "
        f"{(df['unit_price'] < 0).sum()}"
    )

    print(
        f"Missing customer names: "
        f"{df['customer_name'].isna().sum()}"
    )


if __name__ == "__main__":
    run_quality_checks(INPUT_FILE)
