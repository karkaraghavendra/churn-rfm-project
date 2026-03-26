import pandas as pd
from datetime import datetime

df = pd.read_csv("data.csv")
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'])

today = datetime(2024, 3, 20)

df['Recency'] = (today - df['LastPurchaseDate']).dt.days
df['Frequency'] = df['Transactions']
df['Monetary'] = df['Amount']

print("RFM Data:")
print(df[['CustomerID','Recency','Frequency','Monetary']])

df['Churn'] = df['Recency'].apply(lambda x: 1 if x > 60 else 0)

print("\nChurn Prediction:")
print(df[['CustomerID','Churn']])
