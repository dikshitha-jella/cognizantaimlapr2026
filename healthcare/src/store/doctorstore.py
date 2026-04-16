#generate doctors
import faker
import typing
from models.doctor import Doctor

DEPARTMENTS = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics"]

SPECIALIZATIONS = {
    "Cardiology": ["Cardiologist"],
    "Neurology": ["Neurologist"],
    "Orthopedics": ["Orthopedic Surgeon"],
    "Pediatrics": ["Pediatrician"]
}

class DoctorStore:
    def __init__(self, num_doctors: int):
        self.doctors = []
        self.generate_doctors(num_doctors)

    def generate_doctors(self, num_doctors: int):
        fake = faker.Faker()
        for _ in range(num_doctors):
            name = fake.name()
            email = fake.email()
            department = fake.random_element(DEPARTMENTS)
            specialization = fake.random_element(SPECIALIZATIONS[department])
            doctor = Doctor(name, email, specialization, department)
            self.doctors.append(doctor)

    def get_doctors(self) -> typing.List[Doctor]:
        return self.doctors