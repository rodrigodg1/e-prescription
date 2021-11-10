# -*- coding: utf-8 -*-

#NuCypher pyUmbral It is open-source, built with Python, and uses OpenSSL and Cryptography.io



from json import decoder
from prescription import *
from privacy import *
from patient import *
from medication import *
from diagnosis import*
from file_operations import *
from format_transaction_time import *
from filestatistics import *
from show_evaluation import show_evaluation
from write_files import *
from evaluation import *
from data_creation import *
from show_evaluation import *


from colors import *
import string
import random
from random import randrange
import subprocess


patient1 = Privacy()
patient1_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 



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

        #read from file for evaluation
        personal_id_from_sep_file = read_file_for_evaluation("separate-prescription-data/personal_ID/patient_personal_id_of_precription",i,encode_=True)


#EVALUATION
############################################################################################################################################
        #ENCRYPTION , DELEGATION, RE-ENCRYPTION AND DECRYPTION PERSONAL ID

        capsule_personal_id,cipher_patient_personal_id = evaluation_encryption(doctor,personal_id_from_sep_file,patient1_public_key,"PERSONAL_ID")
        kfrags_personal_id = evaluation_delegation(patient1,patient1_secret_key,doctor_public_key,patient1_signer,"PERSONAL_ID")
        cfrags_personal_id = evaluation_reencryption(patient1,capsule_personal_id,kfrags_personal_id,"PERSONAL_ID")
        evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule_personal_id,cfrags_personal_id,cipher_patient_personal_id,"PERSONAL_ID",show=False)

        #create a SEPARATE FILE for PERSONAL ID ENCRYPTED
        create_separate_data(i,"personal_ID/encrypted/","ENCRYPTED_personal_id_of_prescription",cipher_patient_personal_id)     
############################################################################################################################################





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


        #read from file for evaluation
        medication_from_sep_file = read_file_for_evaluation("separate-prescription-data/medication/medication_of_prescription",i,encode_=True)


#EVALUATION
############################################################################################################################################
        #ENCRYPTION , DELEGATION, RE-ENCRYPTION AND DECRYPTION MEDICATION DATA

        capsule_medication,cipher_medication= evaluation_encryption(doctor,medication_from_sep_file,patient1_public_key,"MEDICATION")
        kfrags_medication = evaluation_delegation(patient1,patient1_secret_key,doctor_public_key,patient1_signer,"MEDICATION")
        cfrags_medication = evaluation_reencryption(patient1,capsule_medication,kfrags_medication,"MEDICATION")
        evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule_medication,cfrags_medication,cipher_medication,"MEDICATION",show=False)


        #create a SEPARATE FILE for PERSONAL ID ENCRYPTED
        create_separate_data(i,"medication/encrypted/","ENCRYPTED_medication_of_prescription",cipher_medication)     
############################################################################################################################################

        # diagnosis data
        start_time_for_create_diagnosis_data = time.time()
        diagnosis_data = string.ascii_uppercase
        #min  char
        #min = max_character_diagnosis / 150
        min = 500
        number_of_characters = randrange(min,max_character_diagnosis)
        diagnosis_data = ''.join(random.choice(diagnosis_data) for i in range(number_of_characters))
        diagnosis = create_diagnosis_data(diagnosis_data)
       # diagnosis = diagnosis.encode()
        end_time_for_create_diagnosis_data = time.time() - start_time_for_create_diagnosis_data
        print(f"\nTime for create DIAGNOSIS data of Prescription {i} in s : {end_time_for_create_diagnosis_data} \n")


        #create a SEPARATE FILE for DIAGNOSIS PLAIN TEXT
        create_separate_data(i,"diagnosis/","diagnosis_of_prescription",diagnosis)

        #read from file for evaluation
        diagnosis_from_sep_file = read_file_for_evaluation("separate-prescription-data/diagnosis/diagnosis_of_prescription",i,encode_=True)


#EVALUATION
############################################################################################################################################
        #ENCRYPTION , DELEGATION, RE-ENCRYPTION AND DECRYPTION DIAGNOSIS DATA

        capsule_diagnosis,cipher_diagnosis= evaluation_encryption(doctor,diagnosis_from_sep_file,patient1_public_key,"DIAGNOSIS")
        kfrags_diagnosis = evaluation_delegation(patient1,patient1_secret_key,doctor_public_key,patient1_signer,"DIAGNOSIS")
        cfrags_diagnosis = evaluation_reencryption(patient1,capsule_diagnosis,kfrags_diagnosis,"DIAGNOSIS")

        evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule_diagnosis,cfrags_diagnosis,cipher_diagnosis,"DIAGNOSIS",show=False)

        #create a SEPARATE FILE for PERSONAL ID ENCRYPTED
        create_separate_data(i,"diagnosis/encrypted/","ENCRYPTED_diagnosis_of_prescription",cipher_diagnosis)     
############################################################################################################################################



        #create the prescription with CLEAR TEXT 
        prescription_with_clear_text = Prescription(patient_personal_id,medication_and_dosage,diagnosis)

        #create the prescription file with CLEAR TEXT 
        prescription = f"prescription-files/prescription{i}"
        with open(prescription, 'w') as f:
            #corresponding to personal data
            f.write(str(prescription_with_clear_text.get_prescription()[0]))
            f.write(",")
            f.write("\n")
            #corresponding to the medication 
            f.write(str(prescription_with_clear_text.get_prescription()[1]))
            f.write(",")
            f.write("\n")
            #corresponding to the diagnosis 
            f.write(str(prescription_with_clear_text.get_prescription()[2]))


        #read prescription file for evaluation
        prescription_to_evaluate = read_file_for_evaluation("prescription-files/prescription",i,encode_=True)


       #evaluate the full prescription
        capsule_prescription,cipher_prescription= evaluation_encryption(doctor,prescription_to_evaluate,patient1_public_key,"FULL_PRESCRIPTION")
        kfrags_prescription = evaluation_delegation(patient1,patient1_secret_key,doctor_public_key,patient1_signer,"FULL_PRESCRIPTION")
        cfrags_prescription = evaluation_reencryption(patient1,capsule_prescription,kfrags_prescription,"FULL_PRESCRIPTION")

        evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule_prescription,cfrags_prescription,cipher_prescription,"FULL_PRESCRIPTION",show=False)





        #create the prescription with ENCRYPTED data
        prescription_with_data_encrypted = Prescription(cipher_patient_personal_id,cipher_medication,cipher_diagnosis)

        #save the prescription with encrypted data in a file
        enc_prescription = f"encrypted-prescription-files/enc_prescription{i}"
        with open(enc_prescription, 'w') as f:
            #corresponding to personal data
            f.write(str(prescription_with_data_encrypted.get_prescription()[0]))
            f.write(",")
            f.write("\n")
            #corresponding to the medication 
            f.write(str(prescription_with_data_encrypted.get_prescription()[1]))
            f.write(",")
            f.write("\n")
            #corresponding to the diagnosis 
            f.write(str(prescription_with_data_encrypted.get_prescription()[2]))






    create_file_with_size("separate-prescription-data/personal_ID/","patient_personal_id_of_precription","report/CLEAR_TEXT_personal_id_size_in_kb",kb=True)
    create_file_with_size("separate-prescription-data/medication/","medication_of_prescription","report/CLEAR_TEXT_medication_size_in_kb",kb=True)
    create_file_with_size("separate-prescription-data/diagnosis/","diagnosis_of_prescription","report/CLEAR_TEXT_diagnosis_size_in_kb",kb=True)



    #create a file with the clear text prescriptions sizes 
    #source to count , file_name_to_count , destination to save
    #print("\n For CLEAR TEXT PRESCRIPTION SIZE:")
    create_file_with_size("prescription-files/","prescription","report/CLEAR_TEXT_prescription_size_in_kb",kb=True)
    
    #create a file with the encrypted prescriptions sizes 
    #print("\n For ENCRYPTED PRESCRIPTION SIZE:")
    create_file_with_size("encrypted-prescription-files/","enc_prescription","report/ENCRYPTED_prescription_size_in_kb",kb=True)
    
    #create a file with the encrypted medications sizes 
    #print("\n For SEPARATE ENCRYPTED MEDICATION :")
    create_file_with_size("separate-prescription-data/medication/encrypted/","ENCRYPTED_medication_of_prescription","separate-prescription-data/ENCRYPTED_medication_size_in_kb",kb=True)
   
    #create a file with the encrypted diagnosis sizes 
    #print("\n For SEPARATE ENCRYPTED DIAGNOSIS:")
    create_file_with_size("separate-prescription-data/diagnosis/encrypted/","ENCRYPTED_diagnosis_of_prescription","separate-prescription-data/ENCRYPTED_diagnosis_size_in_kb",kb=True)
   
    #create a file with the encrypted personal_ID sizes  
    #print("\n For SEPARATE ENCRYPTED PERSONAL ID:")
    create_file_with_size("separate-prescription-data/personal_ID/encrypted/","ENCRYPTED_personal_id_of_prescription","separate-prescription-data/ENCRYPTED_personal_ID_size_in_kb",kb=True)






while(True):
    op = input("\n1 - Create Prescriptions\n2 - Clear Results\n3 - Show All \n4 - Show Evaluation\n> ")

    if(op == "1"):
        try:
            #number_of_diagnosis_char = int(input("Diagnosis size (default = 900000): "))

            number_of_prescriptions = int(input("Number of prescriptions: "))
            number_of_diagnosis_char = 9000000
            create_data_prescription_random(number_of_prescriptions,number_of_diagnosis_char)
            print(f"{bcolors.OKGREEN}\nSuccess !!!{bcolors.ENDC}")
        except Exception as e:
            print(e)
           

    if(op == "2"):
        #call shell script to remove last evaluation
        try:
            subprocess.call(['sh', './reset-evaluations.sh'])
            print(f"{bcolors.OKGREEN}\nSuccess !!!{bcolors.ENDC}")
        except Exception as e:
            print(e)

    if(op == "3"):
        file_numbers = count_files_in_directory("prescription-files/")
        print(f"\n##### Total of prescriptions: {file_numbers} #####")
        for p in range(0,file_numbers):
            print("\n")
            prescription = open_file(f"prescription-files/prescription{p}")
            print(prescription)   

    if(op == "4"):
        show_evaluation()
         
















