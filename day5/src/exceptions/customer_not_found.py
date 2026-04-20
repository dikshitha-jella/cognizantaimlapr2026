class CustomerNotFound(Exception):
    """Exception raised when a customer is not found in the system."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.message = f"Customer with ID '{customer_id}' not found."
        super().__init__(self.message)