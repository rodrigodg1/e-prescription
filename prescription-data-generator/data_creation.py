
from patient import *
from medication import *
from diagnosis import *


#receives the patient's personal data and returns a dictionary as a string
def create_patient_data(name,age):
    patient_data = Patient(f"{name}",f"{age}")

    personal_id = f'"{patient_data.get_name()},{patient_data.get_age()}"'
    
    return personal_id


#receives the patient's medication and returns a dictionary as a string
def create_medication_data(medication,dosage):
    medication_data = Medication(f"{medication}",f"{dosage}")

    medication_and_dosage = f'"{medication_data.get_medication()},{medication_data.get_dosage()}"'

    return medication_and_dosage


#receives the patient's diagnosis and returns a dictionary as a string
def create_diagnosis_data(diagnosis):
    diagnosis_data = Diagnosis(f"{diagnosis}")

    diagnosis_data_ = f'"{diagnosis_data.get_diagnosis()}"'

    return diagnosis_data_


