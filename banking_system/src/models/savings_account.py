from .account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, customer, balance=0.0, interest_rate=0.01, withdrawal_limit=5):
        super().__init__(account_number, customer, balance, "Savings")
        self.interest_rate = interest_rate
        self.withdrawal_limit = withdrawal_limit
        self.withdrawal_count = 0

    def deposit(self, amount):
        if amount > 0 and self.is_active:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.is_active and self.balance >= amount and self.withdrawal_count < self.withdrawal_limit:
            self.balance -= amount
            self.withdrawal_count += 1
            return True
        return False

    def apply_interest(self):
        """Apply interest to the balance"""
        self.balance += self.balance * self.interest_rate

    def reset_withdrawal_count(self):
        """Reset the withdrawal count (monthly)"""
        self.withdrawal_count = 0

    def get_interest_rate(self):
        """Get the interest rate"""
        return self.interest_rate

    def set_interest_rate(self, rate):
        """Set the interest rate"""
        self.interest_rate = rate