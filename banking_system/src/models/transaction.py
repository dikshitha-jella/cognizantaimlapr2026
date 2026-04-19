from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, account, amount, transaction_type):
        self.transaction_id = transaction_id
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type  # 'deposit', 'withdraw', 'transfer', etc.
        self.timestamp = datetime.now()
        self.status = "completed"

    def get_transaction_id(self):
        """Get transaction ID"""
        return self.transaction_id

    def get_amount(self):
        """Get the amount"""
        return self.amount

    def get_transaction_type(self):
        """Get the transaction type"""
        return self.transaction_type

    def get_timestamp(self):
        """Get the timestamp"""
        return self.timestamp

    def get_status(self):
        """Get the status"""
        return self.status

    def set_status(self, status):
        """Set the status"""
        self.status = status

    def __str__(self):
        return f"Transaction({self.transaction_id}, {self.account.account_number}, {self.amount}, {self.transaction_type}, {self.timestamp})"