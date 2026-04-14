# creating entry point for the application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView
""""
creating entry point for the application to display a random name. This is just a sample code to demonstrate the use of faker library.
call the customer view to display customer details. This is just a sample code to demonstrate the use of faker library.
"""


def check():
    """
    This function creates an instance of the Faker class and prints a random name.
    invoke customer view to display customer details
    """
    customer_store = CustomerStore(num_customers=100)
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()


if __name__ == "__main__":
    check()
