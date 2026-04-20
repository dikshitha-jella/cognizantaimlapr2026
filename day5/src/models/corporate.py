#create corporate class using pydantic
from pydantic import Field
from src.models.customer import Customer
from src.models.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str=Field(..., description="Registration number of the company")