# 📚 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 🗂️ Load the Data
df = pd.read_csv(r"C:\Users\lalkesh yaduvanshi\Documents\upi_transactions_2024.CSV")

# 🧮 Convert and Extract Time Features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
df['month'] = df['timestamp'].dt.to_period('M').astype(str)
df['day_of_week'] = df['timestamp'].dt.day_name()
df['hour_of_day'] = df['timestamp'].dt.hour

# 🔥 1. Heatmap: Day vs Hour
heatmap_data = df.groupby(['day_of_week', 'hour_of_day']).size().unstack(fill_value=0)
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d')
plt.title("Transactions Heatmap: Day of Week vs Hour")
plt.ylabel("Day of Week")
plt.xlabel("Hour of Day")
plt.tight_layout()
plt.savefig("heatmap_transactions.png")
plt.show()

# 📊 2. Interactive Bar Chart: Merchant Category Spending
category_amount = df.groupby('merchant_category')['amount (INR)'].sum().sort_values(ascending=False).reset_index()
fig1 = px.bar(category_amount, x='merchant_category', y='amount (INR)',
              title='Total Spending by Merchant Category',
              labels={'amount (INR)': 'Amount (INR)'}, template='plotly_dark')
fig1.write_html("barplot_merchant_category.html")
fig1.show()

# 📈 3. Line Chart: Monthly Spending Trend
monthly_trend = df.groupby('month')['amount (INR)'].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_trend, x='month', y='amount (INR)', marker='o')
plt.title("Monthly UPI Spending Trend")
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Amount (INR)")
plt.tight_layout()
plt.savefig("linechart_monthly_spending.png")
plt.show()

# 📊 4. Stacked Bar Chart: Transaction Type by Day
stacked_data = df.groupby(['day_of_week', 'transaction type']).size().unstack(fill_value=0)
stacked_data.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.title("Transaction Type by Day of Week")
plt.xlabel("Day")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("stackedbar_transaction_type_by_day.png")
plt.show()

# 📍 5. Histogram: Transaction Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['amount (INR)'], kde=True, bins=30, color='teal')
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount (INR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_transaction_amount.png")
plt.show()

# 🥧 6. Pie Chart: Transaction Type Distribution
txn_type_count = df['transaction type'].value_counts().reset_index()
txn_type_count.columns = ['transaction type', 'count']
fig2 = px.pie(txn_type_count, names='transaction type', values='count',
              title='Transaction Type Breakdown')
fig2.write_html("piechart_transaction_type.html")
fig2.show()

# 📦 7. Box Plot: Spending Variation by Merchant Category
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='merchant_category', y='amount (INR)')
plt.xticks(rotation=45)
plt.title("Transaction Amount by Merchant Category")
plt.tight_layout()
plt.savefig("boxplot_merchant_category.png")
plt.show()

# 🌳 8. Treemap: Category Spending Visual
fig3 = px.treemap(category_amount, path=['merchant_category'], values='amount (INR)',
                  title="Treemap: Spending by Merchant Category")
fig3.write_html("treemap_merchant_category.html")
fig3.show()
