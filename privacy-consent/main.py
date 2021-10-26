# -*- coding: utf-8 -*-

from prescription import *
from privacy import *
from patient import *
from medication import *
from diagnosis import*
from file_operations import *
from format_transaction_time import *
from write_files import *


import json
import string
import random
from random import randrange
import subprocess



patient1 = Privacy()
patient_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 





#recebe os dados pessoais do paciente e retorna um dicionario como string
def create_patient_data(name,age):
    
    patient_data = Patient(f"{name}",f"{age}")
    personal_id =  {
        'name': patient_data.get_name(),
        'age': patient_data.get_age()
    }
    
    #convert json to string
    personal_id = json.dumps(personal_id)

    return personal_id

def create_medication_data(medication,dosage):
    
    medication_data = Medication(f"{medication}",f"{dosage}")
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




def create_file_with_prescription_size(path_origin,path_destination):
    count_prescription_files = count_files_in_directory("prescription-files/")
    for p in range (0,count_prescription_files):
            prescription_file_size = file_size(f"{path_origin}{p}")
            write_prescription_size(f"{path_destination}",prescription_file_size)











def create_data_prescription_random(n,doctor,patient_public_key,max_character_diagnosis):

    for prescricao in range(0,n):
        print(f"Prescription {prescricao}")
        #patient Data
        #name = max 25 character
        #age = 18 up to 99
        patient_name = string.ascii_lowercase
        patient_name = ''.join(random.choice(patient_name) for i in range(25))
        patient_age = randrange(18,99)
        patient_personal_id = create_patient_data(patient_name,patient_age)
        patient_personal_id = patient_personal_id.encode()

        #criptografar dados pessoais do paciente
        capsule_patient_personal_id,cipher_patient_personal_id = doctor.encryption(patient_personal_id,patient_public_key)



        #medication data
        #medication name max 50 char
        #dosage min 1 up to 1000
        medication_name = string.ascii_lowercase
        medication_name = ''.join(random.choice(medication_name) for i in range(50))
        dosage = randrange(1,1000)
        medication_and_dosage = create_medication_data(medication_name,dosage)
        medication_and_dosage = medication_and_dosage.encode()


        #criptografar dados da medicação
        capsule_medication_and_dosage,cipher_medication_and_dosage = doctor.encryption(medication_and_dosage,patient_public_key)


        # diagnosis data
        diagnosis_data = string.ascii_lowercase
        #min 100 char
        number_of_characters = dosage = randrange(100,max_character_diagnosis)
        diagnosis_data = ''.join(random.choice(diagnosis_data) for i in range(number_of_characters))
        diagnosis = create_diagnosis_data(diagnosis_data)
        diagnosis = diagnosis.encode()

        #criptografar diagnóstico
        capsule_diagnosis,cipher_diagnosis = doctor.encryption(diagnosis,patient_public_key)



        prescription_with_clear_text = Prescription(patient_personal_id,medication_and_dosage,diagnosis)
        prescription = f"prescription-files/prescription{prescricao}"
        with open(prescription, 'w') as f:
            #correspondente aos dados pessoais
            f.write(str(prescription_with_clear_text.get_prescription()[0]))
            f.write(",")
            f.write("\n")
            #correspondente ao medicamento
            f.write(str(prescription_with_clear_text.get_prescription()[1]))
            f.write(",")
            f.write("\n")
            #correspondente ao diagnóstico
            f.write(str(prescription_with_clear_text.get_prescription()[2]))






        #criar a prescrição com os dados criptografados 
        prescription_with_data_encrypted = Prescription(cipher_patient_personal_id,cipher_medication_and_dosage,cipher_diagnosis)

        #salva a prescrição com os dados criptografados dentro do diretorio
        prescription = f"encrypted-prescription-files/enc_prescription{prescricao}"
        with open(prescription, 'w') as f:
            #correspondente aos dados pessoais
            f.write(str(prescription_with_data_encrypted.get_prescription()[0]))
            f.write(",")
            f.write("\n")
            #correspondente ao medicamento
            f.write(str(prescription_with_data_encrypted.get_prescription()[1]))
            f.write(",")
            f.write("\n")
            #correspondente ao diagnóstico
            f.write(str(prescription_with_data_encrypted.get_prescription()[2]))



    create_file_with_prescription_size("prescription-files/prescription","report/prescription_size_clear_text_in_bytes")
    create_file_with_prescription_size("encrypted-prescription-files/enc_prescription","report/prescription_size_encrypted_in_bytes")





"""

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


"""








while(True):
    op = input("1 - Create Prescriptions\n2 - Clear Results\n3 - Show All \n> ")

    if(op == "1"):
        try:
            number_of_prescriptions = int(input("Number of prescriptions: "))
            create_data_prescription_random(number_of_prescriptions,doctor,patient1_public_key,5000)
            #print("Success !!!\n")
        except Exception as e:
            print(e)
           # print("Error in prescription creation\n")

    if(op == "2"):
        #call shell script to remove last evaluation
        try:
            subprocess.call(['sh', './reset-evaluations.sh'])
            print("Success !!!")
        except Exception as e:
            print(e)

    if(op == "3"):
        file_numbers = count_files_in_directory("prescription-files/")
        print(f"\n##### Total of prescriptions: {file_numbers} #####")
        for p in range(0,file_numbers):
            print("\n")
            prescription = open_file(f"prescription-files/prescription{p}")
            print(prescription)
            print(file_size(f"prescription-files/prescription{p}"))



create_data_prescription_random(3,doctor,patient1_public_key)



#print(my_text)
    
        
