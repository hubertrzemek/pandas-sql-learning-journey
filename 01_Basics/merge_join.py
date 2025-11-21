import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3,],
    'name': ['Alicja', 'Bartek', 'Celina']
})

orders = pd.DataFrame({
    "order_id": [100, 101, 102],
    "customer_id": [1, 2, 1],
    "amount": [50, 120, 30]
})

merged = customers.merge(orders, on="customer_id", how="left")
print(merged)

#Join types: inner, left, right, outer