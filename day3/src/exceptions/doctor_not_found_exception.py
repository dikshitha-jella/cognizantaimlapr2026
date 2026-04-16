"""
create doctor not found exception
"""

class DoctorNotFoundException(Exception):
    """
    custom exception for doctor not found
    """
    def __init__(self, message="Doctor not found"):
        self.message = message
        super().__init__(self.message)