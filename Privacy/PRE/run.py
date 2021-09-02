from random import randint
from file_operations import file_size
import json,os,glob
import tracemalloc
import time
from file_operations import *
from create_prescription import *
from write_files import *

from umbral import pre, keys, signing
# Generate Umbral keys for Alice,
alices_private_key = keys.UmbralPrivateKey.gen_key()
alices_public_key = alices_private_key.get_pubkey()

alices_signing_key = keys.UmbralPrivateKey.gen_key()
alices_verifying_key = alices_signing_key.get_pubkey()
alices_signer = signing.Signer(private_key=alices_signing_key)

# Generate Umbral keys for Bob,
bobs_private_key = keys.UmbralPrivateKey.gen_key()
bobs_public_key = bobs_private_key.get_pubkey()


op = input("1 - run evaluations\n2 - clear evaluations directory: ")


if (op == "1"):


    try:
        #number of prescription to analyse
        number_prescriptions = 0
        number_prescriptions = int(input("numbers of prescriptions: "))

        #loop for create prescription
        #size is a number of chars
        for i in range (1,number_prescriptions+1):
            dosage_size = randint(1,2)
            medication_size = randint(30,200)
            diagnosis_size = randint(80,10000)
            create_prescriptions(i,diagnosis_size,medication_size,dosage_size)


        #read the prescriptions
        for i in range (1,number_prescriptions+1):
            #os.system('clear')
            #print("\n----------------------------------------------------------------------------------------------------------------")
            print(f"Prescription {i}")
            precription_file_name = f"prescriptions-files/prescription{i}"
            prescription = open_file(precription_file_name)
            print(prescription)
            print("\n")
            prescription_file_size = file_size(precription_file_name)

            #print(f"Prescription {i} File Size is :", prescription_file_size, "bytes")

            #store on file
            path = "report/prescriptions_size_in_bytes.txt"
            write_prescription(path,prescription_file_size)


            #time.sleep(1)

            start_time_total_execution = time.time()

            start_time = time.time() # time execution
            tracemalloc.start() # memory usage


            # Encrypt data with Alice's public key,
            #convert string to bytes
            plaintext = prescription.encode()
            ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)
            #print("\nEncrypted Prescription: ", ciphertext)
            enc_prescription = f"encrypted-prescription-files/enc_prescription{i}"
            with open(enc_prescription, 'w') as f:
                f.write('"'+str(ciphertext)+'"')
                f.write(',')
                f.write("\n")
                f.write('"'+str(capsule)+'"')
                
                f.write("\n")

            #default is bytes
            current, peak = tracemalloc.get_traced_memory()
            #print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
            #print(f"\nMemory usage for encryption is {current/1024} KiB; Peak was {peak/1024} KiB")
            tracemalloc.stop()

            

            #write size of encripted prescription in file
            enc_precription_file_name = f"encrypted-prescription-files/enc_prescription{i}"
            enc_prescription = open_file(enc_precription_file_name)
            encripted_prescription_file_size = file_size(enc_precription_file_name)
            path = "report/encripted_prescriptions_size_in_bytes.txt"
            write_prescription(path,encripted_prescription_file_size)


            #print(f"Time execution for encryption in s: {time.time() - start_time}")

            #store the memory usage in file
            path = "report/memory-evaluation/encryption_memory_usage_in_kB.txt"
            write_memory_usage(path,peak)

            #store the execution time in file
            path = "report/execution-time-evaluation/encryption_execution_time_in_s.txt"
            write_execution_time(path,time.time() - start_time)




            # Decrypt data with Alice's private key,
            #cleartext = pre.decrypt(ciphertext=ciphertext,
            #                        capsule=capsule.
            #                        decrypting_key=alices_private_key)

            # Alice generates "M of N" re-encryption key fragments (or "KFrags") for Bob,
            # In this example, 10 out of 20,
            #time.sleep(1)

            start_time = time.time() # time execution
            tracemalloc.start()

            kfrags = pre.generate_kfrags(delegating_privkey=alices_private_key,
                                        signer=alices_signer,
                                        receiving_pubkey=bobs_public_key,
                                        threshold=5,
                                        N=10)

            current, peak = tracemalloc.get_traced_memory()
            #print(f"\nMemory usage for create delegation keys is {current/1024} KiB; Peak was {peak/1024} KiB")
            tracemalloc.stop()
            #print(f"Time execution for create delegation keys in s: {time.time() - start_time}")

            

            #store the memory usage in file
            path = "report/memory-evaluation/memory_usage_delegation_key_in_kB.txt"
            write_memory_usage(path,peak)

            #store the execution time in file
            path = "report/execution-time-evaluation/execution_time_delegation_key_in_s.txt"
            write_execution_time(path,time.time() - start_time)


            #time.sleep(1)

            # Several Ursulas perform re-encryption, and Bob collects the resulting `cfrags`,
            # He must gather at least `threshold` `cfrags` in order to activate the capsule.

            start_time = time.time()
            tracemalloc.start()
            capsule.set_correctness_keys(delegating=alices_public_key,
                                    receiving=bobs_public_key,
                                    verifying=alices_verifying_key)


            cfrags = list()           # Bob's cfrag collection
            for kfrag in kfrags[:10]:
                cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
                cfrags.append(cfrag)    # Bob collects a cfrag

            current, peak = tracemalloc.get_traced_memory()
            #print(f"\nMemory usage for collects keys and re-encryption is {current/1024} KiB; Peak was {peak/1024} KiB")
            tracemalloc.stop()    
            #print(f"Time execution for collects keys and re-encryption in s: {time.time() - start_time}")
        



            #store the memory usage in file
            path = "report/memory-evaluation/re-encryption_memory_usage_in_kB.txt"
            write_memory_usage(path,peak)

            #store the execution time in file
            path = "report/execution-time-evaluation/re-encryption_execution_time_in_s.txt"
            write_execution_time(path,time.time() - start_time)


            #time.sleep(1)

            start_time = time.time()
            tracemalloc.start()
            # Bob activates and opens the capsule
            for cfrag in cfrags:
                capsule.attach_cfrag(cfrag)


            bob_cleartext = pre.decrypt(ciphertext=ciphertext,
                                        capsule=capsule,
                                        decrypting_key=bobs_private_key)

            current, peak = tracemalloc.get_traced_memory()                            
            #print(f"\nMemory usage for bob decrypt is {current/1024} KiB; Peak was {peak/1024} KiB")
            tracemalloc.stop()     
            #print(f"Time execution for bob decrypt in s: {time.time() - start_time}")


            #store the memory usage in file
            path = "report/memory-evaluation/decryption_memory_usage_in_kB.txt"
            write_memory_usage(path,peak)

            #store the execution time in file
            path = "report/execution-time-evaluation/decryption_execution_time_in_s.txt"
            write_execution_time(path,time.time() - start_time)


            #print(f"\nTotal execution time {time.time() - start_time_total_execution}s ")
        
            #store the execution time in file
            path = "report/execution-time-evaluation/total_execution_time_in_s,txt"
            write_execution_time(path,time.time() - start_time_total_execution)

           
        print("Evaluations completed !")
    except:
        print("Fail in evaluation")

#remove all evaluations files in report folder         
elif(op=="2"):
    try:
        os.remove('report/prescriptions_size_in_bytes,txt') 
        os.remove('report/encripted_prescriptions_size_in_bytes,txt') 
       # os.remove('time_transaction_formated,txt')

        dir = os.getcwd() + '/report/memory-evaluation/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        
        dir = os.getcwd() + '/report/execution-time-evaluation/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir = os.getcwd() + '/encrypted-prescription-files/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        dir = os.getcwd() + '/prescriptions-files/'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

        print("Evaluations reseted !!!")
    except:
        print("Fail to delete files")
    


