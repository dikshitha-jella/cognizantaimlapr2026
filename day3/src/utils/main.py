import sys
import os
from datetime import datetime
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)

from src.models.person import Person
from src.models.doctor import Doctor
from src.models.staff import Staff
from src.models.role import Role


from conf.logger_conf import setup_logger
logger = setup_logger()

def create_person():
    person = Person(adharCardNo="123456789012", mobileNo=9876543210)
    print(f"Person created with Adhar Card No: {person.adharCardNo} and Mobile No: {person.mobileNo}")
    """
    update mobile number of person
    """
    fake = Faker()
    try:
        person.mobileNo = fake.phone_number()
        logger.info(f"Person updated with new Mobile No: {person.mobileNo}")
    except ValueError as e:
        logger.error(f"Error updating mobile number: {e}")

def create_staff():
    """
    crate a staff instance and print the details
    """
    role=Role(name="Manager", description="Manages the hospital operations")
    staff = Staff(adharCardNumber="123456789012", mobileNo=9876543210, role=role)
    print(f"Staff created with Adhar Card No: {staff.adharCardNo}, Mobile No: {staff.mobileNo} and Role: {staff.role.name}")



if __name__ == "__main__":
    create_person() 
    create_staff()