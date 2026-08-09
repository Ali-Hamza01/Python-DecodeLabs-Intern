# Expense Tracker
# DecodeLabs Project-2
# Python Programming

print("=============================")
print("       Expense Tracker       ")
print("=============================")

total_expenses = 0

number_of_expenses = int(input("Enter the number of expenses you want to track: "))

for i in range(number_of_expenses):
    expense = float(input(f"Enter expense {i + 1}:"))
    total_expenses += expense

print(f"Total expenses: ${total_expenses:}")