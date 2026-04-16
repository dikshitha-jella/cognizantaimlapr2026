#display doctor details
from store.doctorstore import DoctorStore
class DoctorView:
    def __init__(self, doctor_store: DoctorStore):
        self.doctor_store = doctor_store

    def display_doctors(self):
        doctors = self.doctor_store.get_doctors()
        for doctor in doctors:
            print(doctor)