import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "value": [10, 12, 15]
})
# At this point, "date" is just text (string).

print(df.dtypes)

# 2. Convert string dates to datetime
# pd.to_datetime converts strings like "2024-01-01" to real datetime objects.
df["date"] = pd.to_datetime(df["date"])
print(df.dtypes)


# 3. Set the date column as the index
print("DataFrame with datetime index:")
print(df)
print()


# 4. Filtering by date

filtered_from_2nd = df[df["date"] >= "2024-01-02"]
print("Filtered from 2024-01-03 onwards:")
print(filtered_from_2nd)
print()

# select a specific date range usin .loc
range_selection = df.loc["2024-01-01":"2024-01-04"]
print("Range selection from 2024-01-02 to 2024-01-04:")
print(range_selection)
print()
