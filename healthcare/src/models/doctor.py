#define doctor model
import typing
import datetime

class Doctor:
    def __init__(self, name: str, email: str, specialization: str, department: str):
        self.name = name
        self.email = email
        self.specialization = specialization
        self.department = department

    def __str__(self):
        return f"Doctor(name={self.name}, email={self.email}, specialization={self.specialization}, department={self.department})"