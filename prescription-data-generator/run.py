# -*- coding: utf-8 -*-

#NuCypher pyUmbral It is open-source, built with Python, and uses OpenSSL and Cryptography.io

from prescription import *
from patient import *
from medication import *
from diagnosis import*
from file_operations import *
from format_transaction_time import *
from filestatistics import *
from write_files import *
from data_creation import *


from colors import *
import string
import random
from random import randrange
import subprocess


def create_separate_data(i,path,prescription_data_type,data_to_write):
    path = f"separate-prescription-data/{path}{prescription_data_type}{i}"
    with open(path, 'w') as f:
        f.write(str(data_to_write)) 


#create the prescription data and evaluation
def create_data_prescription_random(n,max_character_diagnosis=900000):
    for i in range(0,n):
        print(f"\nPrescription {i}")

        #patient Data
        #name = max 200 character
        #age = 18 up to 99
        patient_name = string.ascii_uppercase
        min = 80
        max = 550
        number_of_characters = randrange(min,max)
        patient_name = ''.join(random.choice(patient_name) for i in range(number_of_characters))
        patient_age = randrange(18,99)
        patient_personal_id = create_patient_data(patient_name,patient_age)


        #create a file with only the patient's personal data
        create_separate_data(i,"personal_ID/","patient_personal_id_of_precription",patient_personal_id)


        #medication data
        #medication name max 100 char
        #dosage min 1 up to 1000
        medication_name = string.ascii_uppercase
        min = 80
        max = 350
        number_of_characters = randrange(min,max)
        medication_name = ''.join(random.choice(medication_name) for i in range(number_of_characters))
        dosage = randrange(1,1000)
        medication_and_dosage = create_medication_data(medication_name,dosage)
        #medication_and_dosage = medication_and_dosage.encode()

        #create a SEPARATE FILE for medication and dosage
        create_separate_data(i,"medication/","medication_of_prescription",medication_and_dosage)





        # diagnosis data
        diagnosis_data = string.ascii_uppercase
        #min  char
        #min = max_character_diagnosis / 150
        min = 200
        number_of_characters = randrange(min,max_character_diagnosis)
        diagnosis_data = ''.join(random.choice(diagnosis_data) for i in range(number_of_characters))
        diagnosis = create_diagnosis_data(diagnosis_data)
       # diagnosis = diagnosis.encode()


        #create a SEPARATE FILE for DIAGNOSIS PLAIN TEXT
        create_separate_data(i,"diagnosis/","diagnosis_of_prescription",diagnosis)



        #create the prescription with CLEAR TEXT 
        prescription_with_clear_text = Prescription(patient_personal_id,medication_and_dosage,diagnosis)

        #create the prescription file with CLEAR TEXT 
        prescription = f"prescription-files/prescription{i}"
        with open(prescription, 'w') as f:
            #corresponding to personal data
            f.write(str(prescription_with_clear_text.get_prescription()[0]))
            f.write("\n")
            #corresponding to the medication 
            f.write(str(prescription_with_clear_text.get_prescription()[1]))
            f.write("\n")
            #corresponding to the diagnosis 
            f.write(str(prescription_with_clear_text.get_prescription()[2]))


        


    create_file_with_size("separate-prescription-data/personal_ID/","patient_personal_id_of_precription","report/CLEAR_TEXT_personal_id_size_in_kb",kb=True)
    create_file_with_size("separate-prescription-data/medication/","medication_of_prescription","report/CLEAR_TEXT_medication_size_in_kb",kb=True)
    create_file_with_size("separate-prescription-data/diagnosis/","diagnosis_of_prescription","report/CLEAR_TEXT_diagnosis_size_in_kb",kb=True)



    #create a file with the clear text prescriptions sizes 
    #source to count , file_name_to_count , destination to save
    #print("\n For CLEAR TEXT PRESCRIPTION SIZE:")
    create_file_with_size("prescription-files/","prescription","report/CLEAR_TEXT_prescription_size_in_kb",kb=True)
    
   




while(True):
    op = input("\n1 - Create Prescriptions\n2 - Clear Results\n> ")

    if(op == "1"):
        try:
            #number_of_diagnosis_char = int(input("Diagnosis size (default = 900000): "))

            number_of_prescriptions = int(input("Number of prescriptions: "))
            #number_of_diagnosis_char = 11000000
            number_of_diagnosis_char = 443
            create_data_prescription_random(number_of_prescriptions,number_of_diagnosis_char)
            print(f"{bcolors.OKGREEN}\nSuccess !!!{bcolors.ENDC}")
        except Exception as e:
            print(e)
           

    if(op == "2"):
        #call shell script to remove last evaluation
        try:
            subprocess.call(['sh', './reset-generated-data.sh'])
            print(f"{bcolors.OKGREEN}\nSuccess !!!{bcolors.ENDC}")
        except Exception as e:
            print(e)














