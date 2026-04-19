from .account import Account


class CurrentAccount(Account):
    def __init__(self, account_number, customer, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_number, customer, balance, "Current")
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount > 0 and self.is_active:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.is_active and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return True
        return False

    def get_overdraft_limit(self):
        """Get the overdraft limit"""
        return self.overdraft_limit

    def set_overdraft_limit(self, limit):
        """Set the overdraft limit"""
        self.overdraft_limit = limit