#create address class associated with customer using pydantic
from pydantic import BaseModel, Field
from src.models.customer import Customer
class Address(BaseModel):
    #associate address with customer
    customer: Customer
    street: str=Field(..., pattern=".*", description="Street address of the customer")
    city: str=Field(..., pattern=".*", description="City of the customer")
    state: str=Field(..., pattern=".*", description="State of the customer")
    zip_code: str=Field(..., pattern=".*", description="ZIP code of the customer")
    country: str=Field(..., pattern=".*", description="Country of the customer")