import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r'C:/Users/FASEEH ALI/Downloads/Amazon Sales data.csv')

# Convert 'order_date' column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month, year, and day from 'order_date' column
df['month'] = df['Order Date'].dt.month
df['year'] = df['Order Date'].dt.year
df['day_name'] = df['Order Date'].dt.day_name()

# Calculate total profit
df['total_profit'] = df['Unit Price'] - df['Unit Cost']

# Month-wise sales trend
month_wise_sales = df.groupby('month')['Units Sold'].sum()
print("Month-wise Sales Trend:")
print(month_wise_sales)

# Year-wise sales trend
year_wise_sales = df.groupby('year')['Units Sold'].sum()
print("\nYear-wise Sales Trend:")
print(year_wise_sales)

# Yearly_month-wise sales trend
yearly_month_wise_sales = df.groupby(['year', 'month'])['Units Sold'].sum()
print("\nYearly_Month-wise Sales Trend:")
print(yearly_month_wise_sales)

# Key metrics and factors
print("\nKey Metrics and Factors:")
print("Unit Price: Min={}, Max={}, Mean={}".format(df['Unit Price'].min(), df['Unit Price'].max(), df['Unit Price'].mean()))
print("Unit Cost: Min={}, Max={}, Mean={}".format(df['Unit Cost'].min(), df['Unit Cost'].max(), df['Unit Cost'].mean()))
print("Total Profit: Min={}, Max={}, Mean={}".format(df['Total Profit'].min(), df['Total Profit'].max(), df['Total Profit'].mean()))
print("Units Sold: Min={}, Max={}, Mean={}".format(df['Units Sold'].min(), df['Units Sold'].max(), df['Units Sold'].mean()))

# Item type distribution
item_type_distribution = df['Item Type'].value_counts()
print("\nItem Type Distribution:")
print(item_type_distribution)

# Region distribution
region_distribution = df['Region'].value_counts()
print("\nRegion Distribution:")
print(region_distribution)

# Shipping day name distribution
shipping_day_name_distribution = df['day_name'].value_counts()
print("\nShipping Day Name Distribution:")
print(shipping_day_name_distribution)

# Plotting the sales trend(Month)
plt.figure(figsize=(10, 6))
month_wise_sales.plot(kind='bar',color='r')
plt.title('Month-wise Sales Trend')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.show()

# Plotting the sales trend(Year)
plt.figure(figsize=(10, 6))
year_wise_sales.plot(kind='bar',color ='g')
plt.title('Year-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Units Sold')
plt.show()

# Plotting the sales trend(yearly_month)
plt.figure(figsize=(10, 6))
yearly_month_wise_sales.unstack().plot(kind='bar')
plt.title('Yearly_Month-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Units Sold')
plt.show()

# Plotting Region Distribution

fields=['Sub-Saharan Africa','Europe','Australia and Oceania','Asia','Middle East and North Africa','Central America and the Caribbean','North America']
div =[36,22,11,11,10,7,3]
plt.pie(div, labels = fields, colors = ['red','green','blue','orange','cyan','yellow','pink'],autopct = '%0.1f%%')
plt.title('Region Distribution')
plt.show()

# Plotting Item type

plt.figure(figsize=(10, 6))
item_type_distribution.plot(kind='bar',color='pink')
plt.title('Item Type Distribution')
plt.xlabel('Item')
plt.ylabel('Units Sold')
plt.show()

# Plotting Shipping Day Distribution

week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
dist=[11,14,18,11,10,19,17]
plt.plot(week,dist,marker = 'o', linestyle = '--')
plt.title('Shipping Day Distribution')
plt.xlabel('Days')
plt.ylabel('Units Sold')
plt.show()
