#display patient details and mappings
from store.patientstore import PatientStore
from store.healthcaremapping import HealthCareMapping

class PatientView:
    def __init__(self, patient_store: PatientStore, mapping: HealthCareMapping):
        self.patient_store = patient_store
        self.mapping = mapping

    def display_patients(self):
        patients = self.patient_store.get_patients()
        for patient in patients:
            print(patient)

    def display_patient_doctor_mapping(self):
        mapped = self.mapping.get_mapped_patients()
        for patient, doctor in mapped.items():
            print(f"{patient.name} ({patient.disease}) -> {doctor.name} ({doctor.specialization})")