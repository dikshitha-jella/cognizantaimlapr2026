"""Test for patient"""

import sys
import os
import pytest
import csv
from datetime import datetime

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)

sys.path.append(project_root)
from src.models.patient import Patient


@pytest.fixture
def initialize_patient():
    patient = Patient(id=1, name="Rajesh Kumar", dob=datetime(1979, 5, 15).date(), ailment="Hypertension")
    return patient


def read_patient_data_from_csv():
    """Read patient data from csv file and return as list of tuples"""
    patient_data = []
    with open('tests/patients.csv', mode='r', newline="", encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            dob = datetime.strptime(row['dob'], '%Y-%m-%d').date()
            patient_data.append((int(row['id']), row['name'], dob, row['ailment']))
    return patient_data


# Test for patient object created
def test_patient_creation(initialize_patient):
    patient = initialize_patient
    assert patient.id == 1
    assert patient.name == "Rajesh Kumar"
    assert patient.dob == datetime(1979, 5, 15).date()
    assert patient.ailment == "Hypertension"


# Parameterized test for patient object created
@pytest.mark.parametrize("id, name, dob, ailment", read_patient_data_from_csv())
def test_patient_creation_parameterized(id, name, dob, ailment):
    patient = Patient(id=id, name=name, dob=dob, ailment=ailment)
    assert patient.id == id
    assert patient.name == name
    assert patient.dob == dob
    assert patient.ailment == ailment
