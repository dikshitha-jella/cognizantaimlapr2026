from abc import ABC, abstractmethod


class ABCBankingGroup(ABC):
    """Abstract base class for banking groups"""
    
    def __init__(self, group_id, group_name):
        self.group_id = group_id
        self.group_name = group_name
        self.customers = []
        self.accounts = []
    
    @abstractmethod
    def add_customer(self, customer):
        """Add a customer to the banking group"""
        pass
    
    @abstractmethod
    def remove_customer(self, customer_id):
        """Remove a customer from the banking group"""
        pass
    
    @abstractmethod
    def get_customer(self, customer_id):
        """Get a customer by ID"""
        pass
    
    def __str__(self):
        return f"ABCBankingGroup({self.group_id}, {self.group_name})"