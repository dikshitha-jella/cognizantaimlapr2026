#generate patients
import faker
import typing
from models.patient import Patient

DISEASE_DEPARTMENT_MAPPING = {
    "Cardiology": ["Heart Attack", "Hypertension", "Arrhythmia"],
    "Neurology": ["Stroke", "Epilepsy", "Parkinson's"],
    "Orthopedics": ["Fracture", "Arthritis", "Back Pain"],
    "Pediatrics": ["Common Cold", "Chickenpox", "Asthma"]
}

class PatientStore:
    def __init__(self, num_patients: int):
        self.patients = []
        self.generate_patients(num_patients)

    def generate_patients(self, num_patients: int):
        fake = faker.Faker()
        for _ in range(num_patients):
            name = fake.name()
            email = fake.email()
            dob = fake.date_of_birth()
            # Randomly select a department and then a disease
            department = fake.random_element(list(DISEASE_DEPARTMENT_MAPPING.keys()))
            disease = fake.random_element(DISEASE_DEPARTMENT_MAPPING[department])
            patient = Patient(name, email, dob, disease)
            self.patients.append(patient)

    def get_patients(self) -> typing.List[Patient]:
        return self.patients

    def get_patients_by_department(self, department: str) -> typing.List[Patient]:
        return [p for p in self.patients if self.get_department_for_disease(p.disease) == department]

    def get_department_for_disease(self, disease: str) -> str:
        for dept, diseases in DISEASE_DEPARTMENT_MAPPING.items():
            if disease in diseases:
                return dept
        return "Unknown"