import pandas as pd

df = pd.read_excel('C:/Users/Seid/Desktop/ecommerce/REVENUE.csv.xlsx')

# 1. Total Revenue
print("TOTAL REVENUE:")
print(round(df['Revenue'].sum(), 2))

# 2. Revenue By Country
print('\nREVENUE BY COUNTRY:')
print(df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10))

#3. Top 10 Customer
print('\nTOP 10 CUSTOMERS:')
print(df[df['Quantity']>0].groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10))

#4. Monthly Revenue
print('\nMONTHLY REVENUE:')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
print(df.groupby('Month')['Revenue'].sum())

# Revenue by Country
df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).reset_index().to_excel('C:/Users/Seid/Desktop/ecommerce/Revenue_by_Country.xlsx', index=False)

# Top 10 Customers
df[df['Quantity'] > 0].groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10).reset_index().to_excel('C:/Users/Seid/Desktop/ecommerce/Top_Customers.xlsx', index=False)

# Monthly Revenue
df.groupby('Month')['Revenue'].sum().reset_index().to_excel('C:/Users/Seid/Desktop/ecommerce/Monthly_Revenue.xlsx', index=False)

print("All saved separately!")