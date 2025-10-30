import pandas as pd  

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
}

# Create DataFrame
df = pd.DataFrame(data)

# shows the first 5 rows 
df.head()
# shows info about columns and data types
df.info()
# statistical summary of numerical columns
df.describe


#access single column
df["Name"]   
print(df["Name"]  )
#access multiple columns
print (df[["Name", "Age"]])

#filter rows where Age > 22
filtered_df = df[df["Age"] > 22]
print(filtered_df)  

# adding a new column
df["City"] = ["New York", "Los Angeles", "Chicago", "Houston"]

#removing a column
print(df)
df = df.drop(columns = ["City"])
print(df)

#sorting values 
sorted_df = df.sort_values(by="Age",ascending=False)
print(sorted_df)

# detect missing values
df.isna()

#fill missing values (example
df.fillna(value= "Unknown", inplace=False)

# export to CSV
df.to_csv("output.csv", index=False)