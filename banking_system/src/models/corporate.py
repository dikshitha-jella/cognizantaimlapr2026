from .customer import Customer


class Corporate(Customer):
    """Corporate customer type"""
    
    def __init__(self, customer_id, name, email, company_name, registration_number):
        super().__init__(customer_id, name, email)
        self.company_name = company_name
        self.registration_number = registration_number
    
    def __str__(self):
        return f"Corporate({self.customer_id}, {self.name}, {self.email}, {self.company_name}, {self.registration_number})"