# Healthcare Management System

A Python-based healthcare application that manages doctors, patients, and maps patients to appropriate doctors based on diseases and medical departments.

## Overview

This project implements a healthcare management system that:
- Generates random doctors with specializations across multiple departments
- Generates random patients with specific diseases
- Automatically maps patients to doctors based on their disease and the corresponding department

## Project Structure

```
healthcare/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── doctor.py          # Doctor model
│   │   └── patient.py         # Patient model
│   ├── store/
│   │   ├── __init__.py
│   │   ├── doctorstore.py     # Doctor data management
│   │   ├── patientstore.py    # Patient data management
│   │   └── healthcaremapping.py # Patient-Doctor mapping logic
│   ├── view/
│   │   ├── __init__.py
│   │   ├── doctorview.py      # Doctor display
│   │   └── patientview.py     # Patient display & mappings
│   ├── app.py                 # Main application logic
│   └── start.py               # Application entry point
├── docs/                       # Sphinx documentation
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## Departments & Specializations

The system includes 4 departments:

### 1. **Cardiology**
- **Specialization**: Cardiologist
- **Diseases**: Heart Attack, Hypertension, Arrhythmia

### 2. **Neurology**
- **Specialization**: Neurologist
- **Diseases**: Stroke, Epilepsy, Parkinson's

### 3. **Orthopedics**
- **Specialization**: Orthopedic Surgeon
- **Diseases**: Fracture, Arthritis, Back Pain

### 4. **Pediatrics**
- **Specialization**: Pediatrician
- **Diseases**: Common Cold, Chickenpox, Asthma

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Navigate to the healthcare directory**:
   ```bash
   cd healthcare
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv healthcareenv
   ```

3. **Activate the virtual environment**:
   ```bash
   source healthcareenv/bin/activate
   ```

4. **Install the project**:
   ```bash
   pip install -e .
   ```

5. **Install development dependencies** (optional, for testing & documentation):
   ```bash
   pip install -e .[dev]
   ```

## Running the Application

### Basic Usage

Run the main application:
```bash
python src/app.py
```

Or using the start module:
```bash
python src/start.py
```

### Example Output

```
Patient-Doctor Mappings:
Rhonda Sellers (Heart Attack) -> Haley Petersen (Cardiologist)
Nicole Wilson (Stroke) -> Gregory Mcdonald DVM (Neurologist)
Haley Harrison (Epilepsy) -> Michael Stevens (Neurologist)
Mary Lara (Arthritis) -> Danielle Sanford (Orthopedic Surgeon)
Kevin Wright (Hypertension) -> David Harris (Cardiologist)
Jeffrey Montes (Common Cold) -> Michael Santos (Pediatrician)
David Ayala (Stroke) -> Gregory Mcdonald DVM (Neurologist)
Elizabeth Smith (Epilepsy) -> Gregory Mcdonald DVM (Neurologist)
Jonathan Thomas (Hypertension) -> Anna Paul (Cardiologist)
Riley Carpenter (Asthma) -> Michael Santos (Pediatrician)
```

## Features

- ✅ Random doctor generation with specializations
- ✅ Random patient generation with diseases
- ✅ Automatic patient-to-doctor mapping based on disease department
- ✅ Clean output format: `patient name (disease) -> doctor name (specialization)`
- ✅ Organized department structure
- ✅ Object-oriented design with models, stores, and views

## Code Examples

### Doctor Model
```python
from models.doctor import Doctor

doctor = Doctor(
    name="John Doe",
    email="john@example.com",
    specialization="Cardiologist",
    department="Cardiology"
)
```

### Patient Model
```python
from models.patient import Patient

patient = Patient(
    name="Jane Smith",
    email="jane@example.com",
    dob="1990-01-01",
    disease="Heart Attack"
)
```

### Using the Stores
```python
from store.doctorstore import DoctorStore
from store.patientstore import PatientStore
from store.healthcaremapping import HealthCareMapping

# Generate data
doctor_store = DoctorStore(num_doctors=20)
patient_store = PatientStore(num_patients=100)

# Map patients to doctors
mapping = HealthCareMapping(doctor_store, patient_store)
mapping.map_patients_to_doctors()
```

## Development

### Code Formatting
```bash
black src/
```

### Import Sorting
```bash
isort src/
```

### Running Tests
```bash
pytest
```

### Building Documentation
```bash
cd docs
make html
```

## Configuration

Modify the number of doctors and patients in `src/app.py`:

```python
doctor_store = DoctorStore(num_doctors=20)      # Change to desired number
patient_store = PatientStore(num_patients=100)  # Change to desired number
```

## Dependencies

### Production
- `faker>=13.3.4` - Generate random data

### Development
- `pytest>=7.2.0` - Testing framework
- `pytest-cov>=3.0.0` - Code coverage reporting
- `black>=23.3.0` - Code formatting
- `isort>=5.10.1` - Import sorting
- `sphinx>=5.0.0` - Documentation generation

## Author

Created by: Dikshitha  
Email: dikshithajella2004@gmail.com

## License

This project is part of the Cognizant AI ML APR 2026 assignment.

## Notes

- Patient-to-doctor assignments are random within each department
- The system generates fake data using the `faker` library
- All names, emails, and DOBs are randomly generated for demo purposes
