"""
create staff store to manage staff data
"""
from src.models.person import Person
from src.models.role import Role

class Staff(Person):
    def __init__(self, adharCardNumber: str, mobileNo: int, role: Role):
        super().__init__(adharCardNumber, mobileNo)
        #associate role with staff
        self.role = role

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, value: Role):
        self.__role = value    