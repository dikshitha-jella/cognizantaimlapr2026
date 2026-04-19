from .transaction import Transaction


class DirectDebit(Transaction):
    """Direct debit transaction type"""
    
    def __init__(self, transaction_id, account, amount, payee, mandate_reference):
        super().__init__(transaction_id, account, amount, "direct_debit")
        self.payee = payee
        self.mandate_reference = mandate_reference
    
    def __str__(self):
        return f"DirectDebit({self.transaction_id}, {self.account.account_number}, {self.amount}, {self.payee}, {self.mandate_reference})"