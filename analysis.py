import pandas as pd
import matplotlib.pyplot as plt

# Load data
expenses = pd.read_csv('expenses1.csv')

# Calculate total spending
total_spending = expenses['Amount'].sum()
# print(f'Total Spending: ${total_spending:.2f}')

# Summarize spending by category
category_summary = expenses.groupby('Category')['Amount'].sum().reset_index()
# print(category_summary)

# Visializing data
# Bar chart of spending by category
plt.figure(figsize=(10, 6))
plt.bar(category_summary['Category'], category_summary['Amount'])
plt.xlabel('Category')
plt.ylabel('Total Spending')
plt.title('Spending by Category')
plt.show()