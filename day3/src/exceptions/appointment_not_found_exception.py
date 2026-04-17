"""
create appointment not found exception
"""

class AppointmentNotFoundException(Exception):
    """
    custom exception for appointment not found
    """
    def __init__(self, message="Appointment not found"):
        self.message = message