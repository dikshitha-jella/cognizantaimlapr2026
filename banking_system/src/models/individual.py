from .customer import Customer


class Individual(Customer):
    """Individual customer type"""
    
    def __init__(self, customer_id, name, email, date_of_birth, ssn):
        super().__init__(customer_id, name, email)
        self.date_of_birth = date_of_birth
        self.ssn = ssn  # Social Security Number
    
    def __str__(self):
        return f"Individual({self.customer_id}, {self.name}, {self.email}, {self.date_of_birth}, {self.ssn})"