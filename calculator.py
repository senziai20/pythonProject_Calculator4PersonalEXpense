import pandas as pd

# Load data
expenses = pd.read_csv('expenses1.csv')

# Calculate total spending
total_spending = expenses['Amount'].sum()
print(f'Total Spending: ${total_spending:.2f}')

# Python 3.5 and Earlier
#  print('Total Spending: ${:.2f}'.format(total_spending))

# Summarize spending by category
category_summary = expenses.groupby('Category')['Amount'].sum().reset_index()
print(category_summary)