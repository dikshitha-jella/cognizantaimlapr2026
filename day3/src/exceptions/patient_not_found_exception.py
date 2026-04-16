"""
create patient not found exception
"""
class PatientNotFoundException(Exception):
    """
    custom exception for patient not found
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
