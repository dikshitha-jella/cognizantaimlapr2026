class Menu:
    """Menu class for banking system UI"""
    
    @staticmethod
    def display_main_menu():
        print("\n===== Banking System Menu =====")
        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. View Customers")
        print("7. View Accounts")
        print("8. View Transactions")
        print("9. Exit")
        print("================================")
        return input("Select an option: ")
    
    @staticmethod
    def display_customer_menu():
        print("\n===== Customer Type Menu =====")
        print("1. Individual")
        print("2. Corporate")
        print("================================")
        return input("Select customer type: ")
    
    @staticmethod
    def display_account_menu():
        print("\n===== Account Type Menu =====")
        print("1. Savings Account")
        print("2. Current Account")
        print("================================")
        return input("Select account type: ")
    
    @staticmethod
    def display_transaction_menu():
        print("\n===== Transaction Type Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Direct Debit")
        print("4. External Transfer")
        print("================================")
        return input("Select transaction type: ")