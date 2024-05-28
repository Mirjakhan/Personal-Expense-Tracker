import csv
import datetime

EXPENSE_FILE = 'expenses.csv'

def add_expense(date, category, amount, description):
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

def view_expenses():
    try:
        with open(EXPENSE_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: ${row[2]}, Description: {row[3]}")
    except FileNotFoundError:
        print("No expenses found. Start by adding a new expense.")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
