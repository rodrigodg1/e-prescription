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



def read_file_for_evaluation(relative_path,i,encode_=True):
        #read from file for evaluation
        with open(f'{relative_path}{i}') as f:
                content = f.readlines()
                
        if(encode_):        
                content = str(content).encode()
                return content
        else:
                content = str(content)
                return content




def evaluation_encryption(doctor,data,patient_public_key,item,show=False):
        #ENCRYPTION 
        tracemalloc.stop()  
        item = item.upper()

        

        #encrypt 
        tracemalloc.start() # start memory allocation
        start_time_encryption = time.time() # start time execution

        #encrypt data
        capsule,cipher= doctor.encryption(data,patient_public_key)
        #default is bytes
        end_time_encryption = time.time() - start_time_encryption
        current, peak = tracemalloc.get_traced_memory()

        print(f"final time encryption: {end_time_encryption * 1000}")
        tracemalloc.stop()


        if(show):
         print("\n")
         print(cipher)         

        #write MEMORY ALLOCATION
        path = f"report/memory-evaluation/{item}_encryption_memory_usage_in_kb.txt"
        write_memory_usage(path,peak,kb=True)

        #write  EXECUTION TIME
        path = f"report/execution-time-evaluation/{item}_encryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_encryption)
        
        return capsule,cipher



def evaluation_delegation(patient1,patient1_secret_key,delegatee_public_key,patient1_signer,item):
        tracemalloc.stop()  
        
        item = item.upper()

        tracemalloc.start() # start memory allocation
        start_time_delegation = time.time() # start time execution

        kfrags = patient1.delegation(patient1_secret_key,delegatee_public_key,patient1_signer)

        end_time_delegation = time.time() - start_time_delegation

        print(f"final time delegation: {end_time_delegation * 1000}")


        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        #write MEMORY ALLOCATION in Delegation and Re-Encryption
        path = f"report/memory-evaluation/{item}_delegation_memory_usage_in_kb.txt"
        write_memory_usage(path,peak,kb=True)

        #write EXECUTION TIME in Delegation and Re-Encryption
        path = f"report/execution-time-evaluation/{item}_delegation_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_delegation)

        return kfrags        




def evaluation_reencryption(patient1,capsule,kfrags,item):
        tracemalloc.stop()  
        item = item.upper()
        tracemalloc.start() # start memory allocation

        start_time_reencryption= time.time() # start time execution



        cfrags = patient1.re_encryption(kfrags,capsule)



        end_time_reencryption = time.time() - start_time_reencryption

        print(f"final time re-encryption: {end_time_reencryption * 1000}")

        
        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()


        #write MEMORY ALLOCATION in Re-Encryption
        path = f"report/memory-evaluation/{item}_reencryption_memory_usage_in_kb.txt"
        write_memory_usage(path,peak,kb=True)

        #write EXECUTION TIME in Delegation and Re-Encryption
        path = f"report/execution-time-evaluation/{item}_reencryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_reencryption)

        return cfrags

############################################################################################################################################



def evaluation_decryption(doctor,doctor_secret_key,patient1_public_key,capsule,cfrags,cipher,item,show=False):
############################################################################################################################################
        #DECRYPTION 
        item = item.upper()

        tracemalloc.start() # start memory allocation
        start_time_decryption = time.time() # start time execution


        clear_text = doctor.decrypt_by_delegatee(doctor_secret_key,patient1_public_key,capsule,cfrags,cipher)


        end_time_decryption = time.time() - start_time_decryption

        print(f"final time decryption: {end_time_decryption * 1000}")

        if(show):
         print("\n")
         print(clear_text)
        

        #default is bytes
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        #write MEMORY ALLOCATION in DECRYPTION
        path = f"report/memory-evaluation/{item}_decryption_memory_usage_in_kb.txt"
        write_memory_usage(path,peak,kb=True)

        #write EXECUTION TIME in DECRYPTION
        path = f"report/execution-time-evaluation/{item}_decryption_execution_time_in_ms.txt"
        write_execution_time_in_ms(path,end_time_decryption)

############################################################################################################################################
