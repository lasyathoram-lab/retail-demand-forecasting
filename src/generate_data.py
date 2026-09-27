import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# -----------------------------
# 1. Create dates
# -----------------------------
dates = pd.date_range(
    start="2022-01-01",
    end="2025-12-31",
    freq="D"
)

# -----------------------------
# 2. Define stores and products
# -----------------------------
stores = ["Store_1", "Store_2", "Store_3", "Store_4", "Store_5"]

products = [
    ("Electronics", "Product_A", 450),
    ("Electronics", "Product_B", 700),
    ("Grocery", "Product_C", 80),
    ("Grocery", "Product_D", 120),
    ("Clothing", "Product_E", 600),
    ("Clothing", "Product_F", 900),
    ("Home", "Product_G", 350),
    ("Home", "Product_H", 500)
]

# -----------------------------
# 3. Create combinations
# -----------------------------
rows = []

for date in dates:

    for store in stores:

        for category, product, price in products:

            # Weekend effect
            weekend_effect = 1.20 if date.dayofweek >= 5 else 1.0

            # Monthly seasonal effect
            month_effects = {
                1: 0.90,
                2: 0.95,
                3: 1.00,
                4: 1.05,
                5: 1.10,
                6: 1.05,
                7: 1.00,
                8: 1.05,
                9: 1.10,
                10: 1.20,
                11: 1.30,
                12: 1.45
            }

            seasonal_effect = month_effects[date.month]

            # Yearly growth
            year_effect = 1 + (date.year - 2022) * 0.05

            # Promotion
            promotion = np.random.choice(
                [0, 1],
                p=[0.75, 0.25]
            )

            promotion_effect = 1.35 if promotion == 1 else 1.0

            # Holiday
            holiday = 1 if date.month == 12 and date.day in [24, 25, 26, 31] else 0

            holiday_effect = 1.30 if holiday == 1 else 1.0

            # Store effect
            store_effects = {
                "Store_1": 1.00,
                "Store_2": 1.15,
                "Store_3": 0.90,
                "Store_4": 1.25,
                "Store_5": 1.05
            }

            store_effect = store_effects[store]

            # Product/category effect
            category_effects = {
                "Electronics": 0.65,
                "Grocery": 1.80,
                "Clothing": 0.75,
                "Home": 1.00
            }

            category_effect = category_effects[category]

            # Base demand
            base_demand = 35

            # Price effect
            price_effect = 1 / (price / 500) ** 0.35

            # Random variation
            noise = np.random.normal(1, 0.12)

            # Calculate units sold
            units_sold = (
                base_demand
                * weekend_effect
                * seasonal_effect
                * year_effect
                * promotion_effect
                * holiday_effect
                * store_effect
                * category_effect
                * price_effect
                * noise
            )

            # Make sure sales are positive whole numbers
            units_sold = max(1, int(round(units_sold)))

            revenue = units_sold * price

            rows.append([
                date,
                store,
                product,
                category,
                price,
                promotion,
                holiday,
                units_sold,
                revenue
            ])

# -----------------------------
# 4. Create DataFrame
# -----------------------------
df = pd.DataFrame(
    rows,
    columns=[
        "Date",
        "Store",
        "Product",
        "Category",
        "Price",
        "Promotion",
        "Holiday",
        "Units_Sold",
        "Revenue"
    ]
)

# -----------------------------
# 5. Save dataset
# -----------------------------
df.to_csv(
    "data/retail_sales.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())