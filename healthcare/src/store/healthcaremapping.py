#map patients to doctors
import typing
from models.doctor import Doctor
from models.patient import Patient
from store.doctorstore import DoctorStore
from store.patientstore import PatientStore

class HealthCareMapping:
    def __init__(self, doctor_store: DoctorStore, patient_store: PatientStore):
        self.doctor_store = doctor_store
        self.patient_store = patient_store
        self.patient_doctor_map = {}

    def map_patients_to_doctors(self):
        doctors_by_dept = {}
        for doctor in self.doctor_store.get_doctors():
            if doctor.department not in doctors_by_dept:
                doctors_by_dept[doctor.department] = []
            doctors_by_dept[doctor.department].append(doctor)

        for patient in self.patient_store.get_patients():
            dept = self.patient_store.get_department_for_disease(patient.disease)
            if dept in doctors_by_dept and doctors_by_dept[dept]:
                # Assign to a random doctor in the department
                import random
                assigned_doctor = random.choice(doctors_by_dept[dept])
                self.patient_doctor_map[patient] = assigned_doctor

    def get_mapped_patients(self) -> typing.Dict[Patient, Doctor]:
        return self.patient_doctor_map