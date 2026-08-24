import csv
import random
import time
from datetime import datetime, timedelta
from pathlib import Path


# Configuration
OUTPUT_FILE = "../data/large_sales.csv"
NUMBER_OF_RECORDS = 1_000_000

CUSTOMERS = [
    (101, "ABC Industries", "India"),
    (102, "Tech Solutions", "USA"),
    (103, "Global Systems", "UK"),
    (104, "Cloud Corp", "India"),
    (105, "Enterprise Ltd", "Australia"),
    (106, "Digital Works", "Germany"),
    (107, "Smart Systems", "USA"),
    (108, "Data Corp", "India"),
    (109, "Tech World", "Canada"),
    (110, "Analytics Ltd", "Singapore"),
]

PRODUCTS = [
    ("Data Platform", "Software", 1200),
    ("Analytics Platform", "Software", 2500),
    ("Data Integration", "Services", 1800),
    ("Cloud Migration", "Services", 3000),
    ("Data Engineering Service", "Services", 2200),
]

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2026, 8, 24)


def random_date():
    """Generate a random date between START_DATE and END_DATE."""

    days = (END_DATE - START_DATE).days

    return (
        START_DATE +
        timedelta(days=random.randint(0, days))
    ).strftime("%Y-%m-%d")


def generate_record(order_id):
    """Generate one synthetic sales record."""

    customer_id, customer_name, country = random.choice(CUSTOMERS)

    product, category, unit_price = random.choice(PRODUCTS)

    quantity = random.randint(1, 10)

    return [
        order_id,
        customer_id,
        customer_name,
        country,
        product,
        category,
        random_date(),
        quantity,
        unit_price,
    ]


def generate_dataset():

    output_path = Path(OUTPUT_FILE)

    # Create data directory if it doesn't exist
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    start_time = time.time()

    print(
        f"Generating {NUMBER_OF_RECORDS:,} "
        "synthetic sales records..."
    )

    with open(
        output_path,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # CSV header
        writer.writerow([
            "order_id",
            "customer_id",
            "customer_name",
            "country",
            "product",
            "category",
            "order_date",
            "quantity",
            "unit_price"
        ])

        for i in range(NUMBER_OF_RECORDS):

            order_id = 100000 + i

            writer.writerow(
                generate_record(order_id)
            )

            # Progress message every 100,000 records
            if (i + 1) % 100_000 == 0:

                print(
                    f"Generated "
                    f"{i + 1:,} records..."
                )

    elapsed_time = time.time() - start_time

    file_size_mb = output_path.stat().st_size / (
        1024 * 1024
    )

    print("\nGeneration completed!")
    print(f"Records: {NUMBER_OF_RECORDS:,}")
    print(f"File: {output_path}")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Generation time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    generate_dataset()
