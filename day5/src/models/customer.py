#create customer class using pydantic

from pydantic import BaseModel
class Customer(BaseModel):
    customer_id: int=Field(..., gt=0, description="Unique identifier for the customer")
    name: FullName
    email: str=Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', description="Email address of the customer")  
    phone_number: int=Field(..., ge=1000000000, le=9999999999, description="Phone number of the customer")
    address: str=Field(..., description="Address of the customer")