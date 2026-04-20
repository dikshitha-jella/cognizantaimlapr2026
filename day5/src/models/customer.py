from pydantic import BaseModel, Field
from models.full_name import FullName

class Customer(BaseModel):
    customer_id: int = Field(..., gt=0, description="Unique identifier for the customer")
    full_name: FullName = Field(..., description="Full name of the customer")
    email: str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', description="Email address of the customer")
    phone_number: int = Field(...,  description="Phone number of the customer")
   