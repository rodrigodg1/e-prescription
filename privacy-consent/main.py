# -*- coding: utf-8 -*-

from prescription import *
from privacy import *
from patient import *
from medication import *
from diagnosis import*
from file_operations import *
from format_transaction_time import *
from statistics import statistics
from write_files import *
from statistics import *

import json
import string
import random
from random import randrange
import subprocess


import tracemalloc
import time


patient1 = Privacy()
patient_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 





#receives the patient's personal data and returns a dictionary as a string
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

def create_separate_data(i,path,prescription_data_type,data_to_write):
    path = f"separate-prescription-data/{path}{prescription_data_type}{i}"
    with open(path, 'w') as f:
        f.write(str(data_to_write)) 






def create_data_prescription_random(n,doctor,patient_public_key,max_character_diagnosis=5000):

    for i in range(0,n):
        print(f"Prescription {i}")
        #patient Data
        #name = max 200 character
        #age = 18 up to 99
        patient_name = string.ascii_uppercase
        patient_name = ''.join(random.choice(patient_name) for i in range(200))
        patient_age = randrange(18,99)
        patient_personal_id = create_patient_data(patient_name,patient_age)
        patient_personal_id = patient_personal_id.encode()


        #create a file with only the patient's personal data
        create_separate_data(i,"personal_ID/","patient_personal_id_of_precription",patient_personal_id)
          


############################################################################################################################################
        #ENCRYPTION PERSONAL ID

        #encrypt personal patient data
        start_time_encryption_personal_ID = time.time() # start time execution
        tracemalloc.start() # start memory allocation
        #encrypt patient personal identification
        capsule_patient_personal_id,cipher_patient_personal_id = doctor.encryption(patient_personal_id,patient_public_key)
        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_encryption_personal_ID = time.time() - start_time_encryption_personal_ID

        #write PERSONAL ID MEMORY USAGE
        path = "report/memory-evaluation/PERSONAL_ID_encryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME
        path = "report/execution-time-evaluation/PERSONAL_ID_encryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_encryption_personal_ID)


        #create a SEPARATE FILE for PERSONAL ID ENCRYPTED
        create_separate_data(i,"personal_ID/encrypted/","ENCRYPTED_personal_id_of_prescription",cipher_patient_personal_id)     
############################################################################################################################################


############################################################################################################################################
        #DELEGATION AND RE-ENCRYPTION PERSONAL ID

        start_time_delegation_and_reencryption_personal_ID = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        cfrags_personal_id = patient1.delegation_and_re_encryption(patient_secret_key,doctor_public_key,patient1_signer,capsule_patient_personal_id)

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_delegation_and_reencryption_personal_ID  = time.time() - start_time_delegation_and_reencryption_personal_ID

        #write PERSONAL ID MEMORY USAGE in Delegation and Re-Encryption
        path = "report/memory-evaluation/PERSONAL_ID_delegation_reencryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in Delegation and Re-Encryption
        path = "report/execution-time-evaluation/PERSONAL_ID_delegation_reencryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_delegation_and_reencryption_personal_ID)

############################################################################################################################################




############################################################################################################################################
        #DECRYPTION PERSONAL ID

        start_time_decryption_personal_ID = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule_patient_personal_id,cfrags_personal_id,cipher_patient_personal_id)
        print("\n")

        print(clear_text)
        

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_decryption_personal_ID  = time.time() - start_time_decryption_personal_ID

        #write PERSONAL ID MEMORY USAGE in DECRYPTION
        path = "report/memory-evaluation/PERSONAL_ID_decryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in DECRYPTION
        path = "report/execution-time-evaluation/PERSONAL_ID_decryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_decryption_personal_ID)

############################################################################################################################################





        





        #medication data
        #medication name max 100 char
        #dosage min 1 up to 1000
        medication_name = string.ascii_uppercase
        medication_name = ''.join(random.choice(medication_name) for i in range(100))
        dosage = randrange(1,1000)
        medication_and_dosage = create_medication_data(medication_name,dosage)
        medication_and_dosage = medication_and_dosage.encode()

        #create a SEPARATE FILE for medication and dosage
        create_separate_data(i,"medication/","medication_of_prescription",medication_and_dosage)

############################################################################################################################################
        #ENCRYPTION MEDICATION DATA

        start_time_encryption_medication = time.time() # execution time
        tracemalloc.start() # memory usage
        capsule_medication_and_dosage,cipher_medication_and_dosage = doctor.encryption(medication_and_dosage,patient_public_key)
        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_encryption_medication = time.time() - start_time_encryption_medication

        #write MEDICATION MEMORY USAGE
        path = "report/memory-evaluation/MEDICATION_encryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        ##write MEDICATION EXECUTION TIME
        path = "report/execution-time-evaluation/MEDICATION_encryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_encryption_medication)


        #create a SEPARATE FILE for MEDICATION ENCRYPTED
        create_separate_data(i,"medication/encrypted/","ENCRYPTED_medication_of_prescription",cipher_medication_and_dosage)
############################################################################################################################################


############################################################################################################################################
        #DELEGATION AND RE-ENCRYPTION MEDICATION DATA

        start_time_delegation_and_reencryption_medication = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        cfrags_medication = patient1.delegation_and_re_encryption(patient_secret_key,doctor_public_key,patient1_signer,capsule_medication_and_dosage)

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_delegation_and_reencryption_medication = time.time() - start_time_delegation_and_reencryption_medication

        #write PERSONAL ID MEMORY USAGE in Delegation and Re-Encryption
        path = "report/memory-evaluation/MEDICATION_delegation_reencryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in Delegation and Re-Encryption
        path = "report/execution-time-evaluation/MEDICATION_delegation_reencryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_delegation_and_reencryption_medication)

############################################################################################################################################




############################################################################################################################################
        #DECRYPTION MEDICATION 

        start_time_decryption_medication = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule_medication_and_dosage,cfrags_medication,cipher_medication_and_dosage)

        print(clear_text)
        

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_decryption_medication = time.time() - start_time_decryption_medication

        #write PERSONAL ID MEMORY USAGE in DECRYPTION
        path = "report/memory-evaluation/MEDICATION_decryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in DECRYPTION
        path = "report/execution-time-evaluation/MEDICATION_decryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_decryption_medication)

############################################################################################################################################









        # diagnosis data
        diagnosis_data = string.ascii_uppercase
        #min 100 char
        number_of_characters = dosage = randrange(100,max_character_diagnosis)
        diagnosis_data = ''.join(random.choice(diagnosis_data) for i in range(number_of_characters))
        diagnosis = create_diagnosis_data(diagnosis_data)
        diagnosis = diagnosis.encode()

        #create a SEPARATE FILE for DIAGNOSIS PLAIN TEXT
        create_separate_data(i,"diagnosis/","diagnosis_of_prescription",diagnosis)




############################################################################################################################################
        #ENCRYPTION DIAGNOSIS 
        start_time_encryption_diagnosis = time.time() # time execution
        tracemalloc.start() # memory usage
        capsule_diagnosis,cipher_diagnosis = doctor.encryption(diagnosis,patient_public_key)
        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_encryption_diagnosis= time.time() - start_time_encryption_diagnosis


        path = "report/memory-evaluation/DIAGNOSIS_encryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)


        #time execution evaluation
        path = "report/execution-time-evaluation/DIAGNOSIS_encryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_encryption_diagnosis)


        #create a SEPARATE FILE for DIAGNOSIS ENCRYPTED
        create_separate_data(i,"diagnosis/encrypted/","ENCRYPTED_diagnosis_of_prescription",cipher_diagnosis)








############################################################################################################################################
        #DELEGATION AND RE-ENCRYPTION DIAGNOSIS DATA

        start_time_delegation_and_reencryption_diagnosis = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        cfrags_diagnosis = patient1.delegation_and_re_encryption(patient_secret_key,doctor_public_key,patient1_signer,capsule_diagnosis)

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_delegation_and_reencryption_diagnosis = time.time() - start_time_delegation_and_reencryption_diagnosis

        #write PERSONAL ID MEMORY USAGE in Delegation and Re-Encryption
        path = "report/memory-evaluation/DIAGNOSIS_delegation_reencryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in Delegation and Re-Encryption
        path = "report/execution-time-evaluation/DIAGNOSIS_delegation_reencryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_delegation_and_reencryption_diagnosis)

############################################################################################################################################




############################################################################################################################################
        #DECRYPTION MEDICATION 

        start_time_decryption_diagnosis = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule_diagnosis,cfrags_diagnosis,cipher_diagnosis)

        print(clear_text)
        

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_decryption_diagnosis = time.time() - start_time_decryption_diagnosis

        #write PERSONAL ID MEMORY USAGE in DECRYPTION
        path = "report/memory-evaluation/DIAGNOSIS_decryption_memory_usage_in_kB.txt"
        write_memory_usage(path,peak)

        #write PERSONAL ID EXECUTION TIME in DECRYPTION
        path = "report/execution-time-evaluation/DIAGNOSIS_decryption_execution_time_in_ms.txt"
        write_execution_time(path,end_time_decryption_diagnosis)

############################################################################################################################################


























        #create the prescription with CLEAR TEXT
        prescription_with_clear_text = Prescription(patient_personal_id,medication_and_dosage,diagnosis)

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






        #create the prescription with ENCRYPTED data
        prescription_with_data_encrypted = Prescription(cipher_patient_personal_id,cipher_medication_and_dosage,cipher_diagnosis)

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

    """
        #salva a prescrição com os dados criptografados em forma binaria dentro do diretorio
        #string para binario
        prescription = f"binary_enc_prescription/bin_enc_prescription{i}"
        file_numbers = count_files_in_directory("encrypted-prescription-files/")

        with open(prescription, 'w') as f:
            for p in range(0,file_numbers):
                prescription_file = open_file(f"encrypted-prescription-files/enc_prescription{p}")
                binary = str_to_binary(prescription_file)
                f.write(binary)
                
        #desfaz binario para string
        prescription = f"binary_enc_to_cipher_prescription/bin_enc_prescription_after_binary{i}"
        file_numbers = count_files_in_directory("binary_enc_prescription/")

        with open(prescription, 'w') as f:
            for p in range(0,file_numbers):
                prescription_file = open_file(f"binary_enc_prescription/bin_enc_prescription{p}")
                chiper = binary_to_str(prescription_file)
                f.write(chiper)
    

    """

    #create a file with the clear text prescriptions sizes 
    #source to count , file_name_to_count , destination to save
    create_file_with_size("prescription-files/","prescription","report/CLEAR_TEXT_prescription_size_in_kb",kb=True)
    
    #create a file with the encrypted prescriptions sizes 
    create_file_with_size("encrypted-prescription-files/","enc_prescription","report/ENCRYPTED_prescription_size_in_kb",kb=True)
    
    #create a file with the encrypted medications sizes 
    create_file_with_size("separate-prescription-data/medication/encrypted/","ENCRYPTED_medication_of_prescription","separate-prescription-data/ENCRYPTED_medication_size_in_bytes")
   
    #create a file with the encrypted diagnosis sizes 
    create_file_with_size("separate-prescription-data/diagnosis/encrypted/","ENCRYPTED_diagnosis_of_prescription","separate-prescription-data/ENCRYPTED_diagnosis_size_in_bytes")
   
    #create a file with the encrypted personal_ID sizes  
    create_file_with_size("separate-prescription-data/personal_ID/encrypted/","ENCRYPTED_personal_id_of_prescription","separate-prescription-data/ENCRYPTED_personal_ID_size_in_bytes")

    



    #create a file with the prescriptions sizes for binary encrypted size
    #create_file_with_prescription_size("binary_enc_prescription/bin_enc_prescription","report/prescription_size_encrypted_binary_in_bytes")

    #1 -> plain text
    #2 -> encrypted_form
    #3 -> binary send to network





while(True):
    op = input("\n1 - Create Prescriptions\n2 - Clear Results\n3 - Show All \n4 - Show Evaluation\n> ")

    if(op == "1"):
        try:
            number_of_prescriptions = int(input("Number of prescriptions: "))
            create_data_prescription_random(number_of_prescriptions,doctor,patient1_public_key,15000)
            print("Success !!!\n")
        except Exception as e:
            print(e)
           

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

    if(op == "4"):
         
         prescription_info = statistics("report/ENCRYPTED_prescription_size_in_bytes")   
         print("\nEncrypted Prescription Info")
         print(f"Min.: {prescription_info[0]*0.001} kb")
         print(f"Max.: {prescription_info[1]*0.001} kb")   
         print(f"Avg.: {prescription_info[2]*0.001} kb")  






         print("#################### Encryption #############################")
         print("")
         print("\nMemory Allocation (kb):")


         memory_evaluation_personal_ID = statistics("report/memory-evaluation/PERSONAL_ID_encryption_memory_usage_in_kB.txt") 
         print("\nPersonal ID")
         print(f"Min.: {memory_evaluation_personal_ID[0]} kb")
         print(f"Max.: {memory_evaluation_personal_ID[1]} kb")   
         print(f"Avg.: {memory_evaluation_personal_ID[2]} kb")  


         memory_evaluation_medication = statistics("report/memory-evaluation/MEDICATION_memory_usage_encryption_in_kB.txt") 
         print("\nMedication and Dosage")
         print(f"Min.: {memory_evaluation_medication[0] } kb")
         print(f"Max.: {memory_evaluation_medication[1] } kb")   
         print(f"Avg.: {memory_evaluation_medication[2] } kb")     



         memory_evaluation_diagnosis = statistics("report/memory-evaluation/DIAGNOSIS_encryption_memory_usage_in_kB.txt") 
         print("\nDiagnosis")
         print(f"Min.: {memory_evaluation_diagnosis[0] } kb")
         print(f"Max.: {memory_evaluation_diagnosis[1] } kb")   
         print(f"Avg.: { memory_evaluation_diagnosis[2] } kb")     


        
         print("\nExecution Time (ms):")


         execution_time_personal_ID = statistics("report/execution-time-evaluation/PERSONAL_ID_execution_time_encryption_in_ms.txt") 
         print("\nPersonal ID")
         print(f"Min.: {execution_time_personal_ID[0]} ms")
         print(f"Max.: {execution_time_personal_ID[1]} ms")   
         print(f"Avg.: {execution_time_personal_ID[2]} ms")  


         execution_time_medication = statistics("report/execution-time-evaluation/MEDICATION_execution_time_encryption_in_ms.txt") 
         print("\nMedication and Dosage")
         print(f"Min.: {execution_time_medication[0] } ms")
         print(f"Max.: {execution_time_medication[1] } ms")   
         print(f"Avg.: {execution_time_medication[2] } ms")     



         execution_time_diagnosis = statistics("report/execution-time-evaluation/DIAGNOSIS_execution_time_encryption_in_ms.txt") 
         print("\nDiagnosis")
         print(f"Min.: {execution_time_diagnosis[0] } ms")
         print(f"Max.: {execution_time_diagnosis[1] } ms")   
         print(f"Avg.: { execution_time_diagnosis[2] } ms")        
         print("#################### End Encryption #############################")
