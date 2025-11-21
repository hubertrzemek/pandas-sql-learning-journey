import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'B'],
    'Value': [10, 20, 5, 15, 30]
})
grouped = df.groupby('Category')["Value"].sum()
print(grouped)  

grouppedby = df.groupby('Category')["Value"].agg(['sum', 'mean', 'max'])
print(grouppedby)
