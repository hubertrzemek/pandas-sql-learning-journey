import pandas as pd

df = pd.DataFrame({
    "City": ["NY", "NY", "LA", "LA"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [100, 150, 80, 200]
})

pivot = df.pivot_table(
    values="Sales",
    index="City",
    columns="Product",
    aggfunc="sum"
)

print(pivot)

