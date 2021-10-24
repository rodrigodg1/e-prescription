# -*- coding: utf-8 -*-

from prescription import *
from privacy import *
from patient import *
from medication import *
from diagnosis import*
import json




patient1 = Privacy()
patient_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 





#recebe os dados pessoais do paciente e retorna um dicionario como string
def create_patient_data(name,age):
    
    patient_data = Patient(f"{name}","{age}")
    personal_id =  {
        'name': patient_data.get_name(),
        'age': patient_data.get_age()
    }
    
    #convert json to string
    personal_id = json.dumps(personal_id)

    return personal_id

def create_medication_data(medication,dosage):
    
    medication_data = Medication(f"{medication}","{dosage}")
    medication_and_dosage =  {
        'medication': medication_data.get_medication(),
        'dosage': medication_data.get_dosage()
    }
    
    #convert json to string
    medication_and_dosage = json.dumps(medication_and_dosage)
    return medication_and_dosage

def create_diagnosis_data(diagnosis):
    
    diagnosis_data = Diagnosis(f"{diagnosis}")
    diagnosis_data_ = {
        'diagnosis': diagnosis_data.get_diagnosis(),
    }
    
    #convert json to string
    diagnosis_data_ = json.dumps(diagnosis_data_)
    return diagnosis_data_





patient1_personal_id = create_patient_data("Rodrigo", "25")
patient1_personal_id = patient1_personal_id.encode()
patient1_medication = create_medication_data("medication xyz", "32g")
patient1_medication = patient1_medication.encode()
patient1_diagnosis = create_diagnosis_data("o paciente 1 tem isso e aquilo apresentando grave ...")
patient1_diagnosis = patient1_diagnosis.encode()






print("antes de criptografar:")
print(patient1_personal_id)
print(patient1_medication)
print(patient1_diagnosis)

print("\ndepois de criptografar personal ID :")
capsule_patient1_personal_id,cipher_patient1_personal_id = doctor.encryption(patient1_personal_id, patient1_public_key)
print(cipher_patient1_personal_id)

print("\ndepois de criptografar medicacao :")
capsule,cipher_patient1_medication = doctor.encryption(patient1_medication, patient1_public_key)
print(cipher_patient1_medication)

print("\ndepois de criptografar diagnosis :")
capsule,cipher_patient1_diagnosis = doctor.encryption(patient1_diagnosis, patient1_public_key)
print(cipher_patient1_diagnosis)


prescription = Prescription(capsule_patient1_personal_id,cipher_patient1_medication, cipher_patient1_diagnosis)   

print("Dados da prescrição Criptografados: ")
print(prescription.get_prescription())
    
    
#my_text = patient_privacy.decrypt(capsule, ciphertext, patient_secret_key)









#print(my_text)
    
        