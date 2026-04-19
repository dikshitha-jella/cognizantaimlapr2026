from models.customer import Customer
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount
from models.transaction import Transaction

class BankingApp:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.transactions = []

    def create_customer(self, customer_id, name, email):
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_savings_account(self, account_number, customer_id, balance=0.0):
        customer = self.customers.get(customer_id)
        if customer:
            account = SavingsAccount(account_number, customer, balance)
            self.accounts[account_number] = account
            return account
        return None

    def create_current_account(self, account_number, customer_id, balance=0.0):
        customer = self.customers.get(customer_id)
        if customer:
            account = CurrentAccount(account_number, customer, balance)
            self.accounts[account_number] = account
            return account
        return None

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.deposit(amount):
            transaction = Transaction(len(self.transactions) + 1, account, amount, 'deposit')
            self.transactions.append(transaction)
            return True
        return False

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account and account.withdraw(amount):
            transaction = Transaction(len(self.transactions) + 1, account, amount, 'withdraw')
            self.transactions.append(transaction)
            return True
        return False

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        return account.get_balance() if account else None