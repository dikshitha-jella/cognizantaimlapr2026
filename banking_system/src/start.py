from app import BankingApp

def main():
    app = BankingApp()

    # Create a customer
    customer = app.create_customer(1, "John Doe", "john@example.com")
    print(f"Created customer: {customer}")

    # Create accounts
    savings = app.create_savings_account("SAV001", 1, 1000.0)
    current = app.create_current_account("CUR001", 1, 500.0)
    print(f"Created savings account: {savings}")
    print(f"Created current account: {current}")

    # Perform transactions
    app.deposit("SAV001", 200.0)
    app.withdraw("CUR001", 100.0)
    print(f"Savings balance: {app.get_balance('SAV001')}")
    print(f"Current balance: {app.get_balance('CUR001')}")

if __name__ == "__main__":
    main()