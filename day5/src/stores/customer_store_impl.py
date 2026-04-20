from src.stores.customer_store import CustomerStore
class CustomerStoreImpl(CustomerStore):
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def update_customer(self, customer_id, customer):
        for i, cust in enumerate(self.customers):
            if cust.customer_id == customer_id:
                self.customers[i] = customer
                return True
        return False

    def delete_customer(self, customer_id):
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                del self.customers[i]
                return True
        return False