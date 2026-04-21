import json
from models.customer import Customer
from models.full_name import FullName
from dataloaders.customer_data_loader import CustomerDataLoader
from stores.customer_store_impl import CustomerStoreImpl

class CustomerJSONDataLoader(CustomerDataLoader):
    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        # Open and load JSON file
        with open(file_path, "r") as f:
            data = json.load(f)

        # Iterate through each customer record
        for row in data:
            customer_id = int(row['customer_id'])
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            phone_no = row['phone_no']

            # Build FullName object
            full_name = FullName(first_name=first_name, last_name=last_name)

            # Build Customer object
            customer = Customer(
                customer_id=customer_id,
                full_name=full_name,
                email=email,
                phone_number=phone_no
            )

            # Add to store
            customer_store.add_customer(customer)
