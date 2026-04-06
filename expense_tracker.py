import csv
import os
from datetime import datetime

expenses = []
budget = 0
FILE_NAME = "expenses.csv"


# ---------------------------
# Load expenses from CSV
# ---------------------------
def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            for exp in expenses:
                exp['amount'] = float(exp['amount'])


# ---------------------------
# Save expenses to CSV
# ---------------------------
def save_expenses():
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved successfully!")


# ---------------------------
# Add expense
# ---------------------------
def add_expense():
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Use YYYY-MM-DD.")

    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })

    print("Expense added successfully!")


# ---------------------------
# View expenses
# ---------------------------
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expense List ---")
    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")


# ---------------------------
# Track budget
# ---------------------------
def track_budget():
    global budget

    if budget == 0:
        budget = float(input("Enter monthly budget: "))

    total = sum(exp['amount'] for exp in expenses)

    print(f"\nTotal spent: ₹{total}")

    if total > budget:
        print("⚠️ You have exceeded your budget!")
    else:
        print(f"✅ You have ₹{budget - total} left for the month.")


# ---------------------------
# Menu
# ---------------------------
def menu():
    while True:
        print("\n====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    load_expenses()
    menu()