from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):
    def __init__(self, account_number, customer, balance=0.0, account_type=""):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.account_type = account_type
        self.created_date = datetime.now()
        self.last_transaction_date = None
        self.is_active = True
        self.transactions = []

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

    def deactivate(self):
        """Deactivate the account"""
        self.is_active = False

    def activate(self):
        """Activate the account"""
        self.is_active = True

    def add_transaction(self, transaction):
        """Add transaction to history"""
        self.transactions.append(transaction)
        self.last_transaction_date = datetime.now()

    def get_transactions(self):
        """Get all transactions"""
        return self.transactions

    def __str__(self):
        return f"Account({self.account_number}, {self.customer}, {self.balance}, {self.account_type})"