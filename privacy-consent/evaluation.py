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



def evaluation_encryption(doctor,data,patient_public_key,item,show=False):
        #ENCRYPTION 

        item = item.upper()

        #encrypt 
        start_time_encryption = time.time() # start time execution
        tracemalloc.start() # start memory allocation
        #encrypt data
        capsule,cipher= doctor.encryption(data,patient_public_key)
        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_encryption = time.time() - start_time_encryption


        if(show):
         print("\n")
         print(cipher)         

        #write MEMORY ALLOCATION
        path = f"report/memory-evaluation/{item}_encryption_memory_usage_in_kB.txt"
        write_memory_usage_in_kb(path,peak)

        #write  EXECUTION TIME
        path = f"report/execution-time-evaluation/{item}_encryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_encryption)
        
        return capsule,cipher


def evaluation_delegation_reencryption(patient1,patient_secret_key,doctor_public_key,patient1_signer,capsule,item):
        item = item.upper()

        start_time_delegation_and_reencryption= time.time() # start time execution
        tracemalloc.start() # start memory allocation


        cfrags = patient1.delegation_and_re_encryption(patient_secret_key,doctor_public_key,patient1_signer,capsule)

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_delegation_and_reencryption = time.time() - start_time_delegation_and_reencryption

        #write MEMORY ALLOCATION in Delegation and Re-Encryption
        path = f"report/memory-evaluation/{item}_delegation_reencryption_memory_usage_in_kB.txt"
        write_memory_usage_in_kb(path,peak)

        #write EXECUTION TIME in Delegation and Re-Encryption
        path = f"report/execution-time-evaluation/{item}_delegation_reencryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_delegation_and_reencryption)

        return cfrags

############################################################################################################################################



def evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule,cfrags,cipher,item,show=False):
############################################################################################################################################
        #DECRYPTION 
        item = item.upper()

        start_time_decryption = time.time() # start time execution
        tracemalloc.start() # start memory allocation


        clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule,cfrags,cipher)
      
        if(show):
         print("\n")
         print(clear_text)
        

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time_decryption = time.time() - start_time_decryption

        #write MEMORY ALLOCATION in DECRYPTION
        path = f"report/memory-evaluation/{item}_decryption_memory_usage_in_kB.txt"
        write_memory_usage_in_kb(path,peak)

        #write EXECUTION TIME in DECRYPTION
        path = f"report/execution-time-evaluation/{item}_decryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_decryption)

############################################################################################################################################
