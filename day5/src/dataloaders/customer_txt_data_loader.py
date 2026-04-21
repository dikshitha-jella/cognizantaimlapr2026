from dataloaders.customer_data_loader import CustomerDataLoader
from stores.customer_store_impl import CustomerStoreImpl
from models.customer import Customer
from models.full_name import FullName


class CustomerTXTDataLoader(CustomerDataLoader):

    def load_data(self, file_path, customer_store: CustomerStoreImpl):
        with open(file_path, 'r') as f:
            content = f.read()

        # Split records by blank lines
        records = content.strip().split("\n\n")

        for record in records:
            lines = record.strip().split("\n")
            data = {}
            for line in lines:
                key, value = line.split(":", 1)
                # Normalize keys to match model fields
                key = key.strip().lower().replace(" ", "_")
                data[key] = value.strip()

            customer_id = int(data['customer_id'])
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            phone_no = data['phone_no']

            full_name = FullName(first_name=first_name, last_name=last_name)

            customer = Customer(
                customer_id=customer_id,
                full_name=full_name,
                email=email,
                phone_number=phone_no
            )

            customer_store.add_customer(customer)
