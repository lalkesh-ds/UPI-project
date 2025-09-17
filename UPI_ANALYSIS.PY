import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
df = pd.read_csv(r"C:\Users\lalkesh yaduvanshi\Documents\upi_transactions_2024.CSV")

# Convert timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
df['month'] = df['timestamp'].dt.to_period('M')
df['day_of_week'] = df['timestamp'].dt.day_name()
df['hour_of_day'] = df['timestamp'].dt.hour

# ---------- Seaborn Heatmap ----------
heatmap_data = df.groupby(['day_of_week', 'hour_of_day']).size().unstack(fill_value=0)
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d')
plt.title("Transactions Heatmap: Day of Week vs Hour")
plt.ylabel("Day of Week")
plt.xlabel("Hour of Day")
plt.tight_layout()
plt.savefig("heatmap_transactions.png")  # 🔽 Save the plot
plt.show()

# ---------- Plotly Interactive Bar ----------
category_amount = df.groupby('merchant_category')['amount (INR)'].sum().sort_values(ascending=False).reset_index()
fig1 = px.bar(category_amount, x='merchant_category', y='amount (INR)',
              title='Total Spending by Merchant Category (Interactive)',
              labels={'amount (INR)': 'Amount (INR)'}, template='plotly_dark')
fig1.write_html("barplot_merchant_category.html")  # 🔽 Save as HTML
fig1.show()

# ---------- Seaborn Histogram ----------
plt.figure(figsize=(8,5))
sns.histplot(df['amount (INR)'], kde=True, bins=30)
plt.title("Distribution of Transaction Amount")
plt.xlabel("Amount (INR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_transaction_amount.png")  # 🔽 Save the plot
plt.show()

# ---------- Plotly Pie Chart ----------
txn_type_count = df['transaction type'].value_counts().reset_index()
txn_type_count.columns = ['transaction type', 'count']
fig2 = px.pie(txn_type_count, names='transaction type', values='count',
              title='Transaction Type Distribution')
fig2.write_html("piechart_transaction_type.html")  # 🔽 Save as HTML
fig2.show()

# ---------- Seaborn Box Plot ----------
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x='merchant_category', y='amount (INR)')
plt.xticks(rotation=45)
plt.title("Transaction Amount by Merchant Category")
plt.tight_layout()
plt.savefig("boxplot_merchant_category.png")  # 🔽 Save the plot
plt.show()
