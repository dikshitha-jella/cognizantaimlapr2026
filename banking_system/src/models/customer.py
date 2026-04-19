from datetime import datetime


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.created_date = datetime.now()
        self.accounts = []
        self.is_active = True

    def get_customer_id(self):
        """Get customer ID"""
        return self.customer_id

    def get_name(self):
        """Get customer name"""
        return self.name

    def get_email(self):
        """Get customer email"""
        return self.email

    def add_account(self, account):
        """Add an account to customer"""
        self.accounts.append(account)

    def get_accounts(self):
        """Get all accounts"""
        return self.accounts

    def deactivate(self):
        """Deactivate the customer"""
        self.is_active = False

    def activate(self):
        """Activate the customer"""
        self.is_active = True

    def is_customer_active(self):
        """Check if customer is active"""
        return self.is_active

    def __str__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email})"