import random
import string
import numpy as np

def generate_text(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) 


def generate_dosage(size=2, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(string.digits) for _ in range(size) ) + 'g'
    

def generate_diagnosis_medication_dosage(diagnosis,medication,dosage):
    return ('"Diagnosis":'+ '"'+(generate_text(diagnosis)+'"'),
            '"Medication":'+ '"'+(generate_text(medication)+'"'),
            '"Dosage":'+ '"'+(generate_dosage(dosage)+'"')
     )


def create_prescriptions(i,diagnosis_,medication_,dosage_):

#for i in range(1,n+1):
    prescription = f"prescriptions-files/prescription{i}"
    prescription = str(prescription)
    diagnosis,medication,dosage = generate_diagnosis_medication_dosage(diagnosis_,medication_,dosage_)
    with open(prescription, 'w') as f:
        #f.write("{")
        f.write(diagnosis)
        f.write(",")
        f.write("\n")
        f.write(medication)
        f.write(",")
        f.write("\n")
        f.write(dosage)
        #f.write("}")


#create_prescriptions(3,200,100,2)