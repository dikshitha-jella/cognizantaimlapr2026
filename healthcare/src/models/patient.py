#define patient model
import typing
import datetime

class Patient:
    def __init__(self, name: str, email: str, dob: datetime.date, disease: str):
        self.name = name
        self.email = email
        self.dob = dob
        self.disease = disease

    def __str__(self):
        return f"Patient(name={self.name}, email={self.email}, dob={self.dob}, disease={self.disease})"