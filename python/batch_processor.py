import pandas as pd
from pathlib import Path


INPUT_FILE = "../data/sample_sales.csv"
OUTPUT_DIRECTORY = "../data/processed"
CHUNK_SIZE = 3


def process_batch(batch):
    """Clean and transform a batch of records."""

    # Remove duplicate orders
    batch = batch.drop_duplicates(subset=["order_id"])

    # Convert date
    batch["order_date"] = pd.to_datetime(
        batch["order_date"],
        errors="coerce"
    )

    # Remove invalid records
    batch = batch[
        (batch["quantity"] > 0) &
        (batch["unit_price"] >= 0)
    ]

    # Calculate revenue
    batch["revenue"] = (
        batch["quantity"] * batch["unit_price"]
    )

    return batch


def main():

    output_path = Path(OUTPUT_DIRECTORY)
    output_path.mkdir(parents=True, exist_ok=True)

    batch_number = 1
    total_records = 0

    for batch in pd.read_csv(
        INPUT_FILE,
        chunksize=CHUNK_SIZE
    ):

        print(f"Processing batch {batch_number}")

        processed_batch = process_batch(batch)

        output_file = (
            output_path /
            f"processed_batch_{batch_number}.csv"
        )

        processed_batch.to_csv(
            output_file,
            index=False
        )

        total_records += len(processed_batch)

        print(
            f"Batch {batch_number}: "
            f"{len(processed_batch)} records processed"
        )

        batch_number += 1

    print("--------------------------------")
    print(f"Total records processed: {total_records}")
    print("Batch processing completed successfully.")


if __name__ == "__main__":
    main()
