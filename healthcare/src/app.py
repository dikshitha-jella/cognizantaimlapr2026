# creating entry point for the healthcare application
import faker
from store.doctorstore import DoctorStore
from store.patientstore import PatientStore
from store.healthcaremapping import HealthCareMapping
from view.doctorview import DoctorView
from view.patientview import PatientView
"""
creating entry point for the application to display doctors and patients.
Map patients to doctors based on diseases and departments.
"""


def check():
    """
    This function creates instances of stores and views, maps patients to doctors, and displays details.
    """
    doctor_store = DoctorStore(num_doctors=10)
    patient_store = PatientStore(num_patients=10)
    mapping = HealthCareMapping(doctor_store, patient_store)
    mapping.map_patients_to_doctors()

    doctor_view = DoctorView(doctor_store)
    patient_view = PatientView(patient_store, mapping)

    print("Patient-Doctor Mappings:")
    patient_view.display_patient_doctor_mapping()


if __name__ == "__main__":
    check()