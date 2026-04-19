from .transaction import Transaction


class ExternalTransaction(Transaction):
    """External transaction type (transfers to other banks)"""
    
    def __init__(self, transaction_id, account, amount, recipient_bank, recipient_account, reference):
        super().__init__(transaction_id, account, amount, "external_transfer")
        self.recipient_bank = recipient_bank
        self.recipient_account = recipient_account
        self.reference = reference
    
    def __str__(self):
        return f"ExternalTransaction({self.transaction_id}, {self.account.account_number}, {self.amount}, {self.recipient_bank}, {self.recipient_account}, {self.reference})"