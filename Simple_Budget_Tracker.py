def main():
    try:
        # Ask for the total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))

        # Ask for multiple expenses
        expenses = []
        print("\nEnter your expenses (type 'done' to finish):")
        while True:
            user_input = input("Enter expense: ").strip().lower()
            if user_input == 'done':
                break
            try:
                expense = float(user_input)
                expenses.append(expense)
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")

        # Calculate remaining balance
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses

        # Display remaining balance
        print(f"\nTotal Budget: LKR {total_budget:.2f}")
        print(f"Total Expenses: LKR {total_expenses:.2f}")
        print(f"Remaining Balance: LKR {remaining_balance:.2f}")

        # Warning for low funds
        if remaining_balance < 500:
            print("Warning: Low Funds")

        # Keep the window open
        input("\nPress Enter to exit...")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
