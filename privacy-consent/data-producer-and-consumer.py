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
import pickle

from colors import *
import string
import random
from random import randrange
import subprocess


patient1 = Privacy()
patient1_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


############################ DOCTOR APP ##################################

doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 

personal_info = create_patient_data("Rodrigo",25)
#print(personal_info)
medication_and_dosage = create_medication_data("Medicacao testeee", "25g")
#print(medication_and_dosage)
diagnosis = create_diagnosis_data("dasdashdjakshdjkashdjashdhhddahdj26131278461jhashddas153652173123655sdasdhgahsdt615312536146715231278461263127371864hdjhasdghas25361")


personal_info = personal_info.encode()
medication_and_dosage = medication_and_dosage.encode()
diagnosis = diagnosis.encode()


cypher_personalInfo = doctor.encryption(personal_info,patient1_public_key)
#print(type(cypher_personalInfo[0]))
cypher_medication_and_dosage = doctor.encryption(medication_and_dosage,patient1_public_key)
cypher_diagnosis  = doctor.encryption(diagnosis,patient1_public_key)

capsules = []
#exit()
#will be storage in blockchain
capsule_personal_id = cypher_personalInfo[0]
capsule_medication_and_dosage = cypher_medication_and_dosage[0]
capsule_cypher_diagnosis = cypher_diagnosis[0]



"""
capsules_file = f"test/capsules"
with open(capsules_file, 'w') as f:
    #corresponding to personal data
    f.write(str(capsules[0]))

    f.write("\n")
    #corresponding to the medication 
    f.write(str(capsules[1]))

    f.write("\n")
    #corresponding to the diagnosis 
    f.write(str(capsules[2]))
"""




prescription = Prescription(cypher_personalInfo[1],cypher_medication_and_dosage[1],cypher_diagnosis[1])
#save the prescription with encrypted data in a file
enc_prescription = f"test/enc_prescription"
with open(enc_prescription, 'w') as f:
    #corresponding to personal data
    f.write(str(prescription.get_prescription()[0]))
    #f.write(",")
    f.write("\n")
    #corresponding to the medication 
    f.write(str(prescription.get_prescription()[1]))
    #f.write(",")
    f.write("\n")
    #corresponding to the diagnosis 
    f.write(str(prescription.get_prescription()[2]))






#PATIENT APP
kfrags = patient1.delegation(patient1_secret_key,doctor_public_key,patient1_signer)


with open('test/capsules', 'rb') as config_capsule_file:
 
    # Step 3
    config_dictionary = pickle.load(config_capsule_file)
 
    # After config_dictionary is read from file
    print(type(config_dictionary))





#only personal ID
#capsule = lines[0]



#cfrags = patient1.re_encryption(kfrags,capsule)
