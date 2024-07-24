# User Interface(optional)
# Simple CLI
def add_expense(date, category, amount, description):
    with open('expenses1.csv', 'a') as file:
        file.write(f'{date},{category},{amount},{description}\n')

# Example usage
add_expense('2024-07-03', 'Entertainment', 30.00, 'Movie night')
add_expense('2024-07-03', 'Food', 10.00, 'Lunch')
add_expense('2024-07-03', 'Expense', 35.99, 'Shopping')
add_expense('2024-07-03', 'Transport', 29.92, 'Bus fare')
add_expense('2024-07-03', 'Expense', 50.00, 'Hotel')
add_expense('2024-07-03', 'Income', 830.00, 'Interest')
add_expense('2024-07-03', 'Expense', 11.43, 'Stationery')
add_expense('2024-07-04', 'Expense', 130.00, 'Mountains Tours')