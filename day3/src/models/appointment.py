"""
create appointment
"""
from datetime import datetime, date, time
from .doctor import Doctor
from .patient import Patient
class Appointment:
    """
    appointment class to represent a healthcare appointment
    """
    def __init__(self, id: int, date: date, time: time, doctor: Doctor, patient: Patient):
        self.appointment_id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient
    def __str__(self):
        return f"Appointment(id={self.appointment_id}, date='{self.date}', time='{self.time}', doctor={self.doctor}, patient={self.patient})"