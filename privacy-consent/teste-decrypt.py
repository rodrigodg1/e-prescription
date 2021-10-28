
from prescription import *
from privacy import *
from patient import *
from medication import *
from diagnosis import*
from file_operations import *
from format_transaction_time import *
from write_files import *

import json


patient1 = Privacy()
patient_secret_key,patient1_public_key,patient1_signing_key,patient1_signer,patient1_verifying_key = patient1.create_delegator_keys()


doctor = Privacy()
doctor_secret_key,doctor_public_key = doctor.create_delegatee_keys() 




def create_patient_data(name,age):
    
    patient_data = Patient(f"{name}",f"{age}")
    personal_id =  {
        'name': patient_data.get_name(),
        'age': patient_data.get_age()
    }
    
    #convert json to string
    personal_id = json.dumps(personal_id)

    return personal_id


text = create_patient_data("Rodrigo",25)
text = text.encode()

capsule, cyper = doctor.encryption(text,patient1_public_key)

print(cyper)


cfrags = patient1.delegation_and_re_encryption(patient_secret_key,doctor_public_key,patient1_signer,capsule)

clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule,cfrags,cyper)

print(clear_text)