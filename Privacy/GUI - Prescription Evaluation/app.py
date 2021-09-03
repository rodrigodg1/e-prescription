import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from create_prescription import *
import tracemalloc
import time
from file_operations import *
from create_prescription import *
from write_files import *
from random import randint

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "frontend.ui")


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





class FrontendApp:
    def __init__(self, master=None):
        # build ui
        self.frame6 = tk.Frame(master)
        self.entry_medication = tk.Entry(self.frame6)
        self.entry_medication.configure(width='70')
        self.entry_medication.place(anchor='nw', height='40', relx='0.15', rely='0.05', width='650', x='0', y='0')
        self.lbl_medication = tk.Label(self.frame6)
        self.lbl_medication.configure(text='Medication')
        self.lbl_medication.place(anchor='nw', relx='0.02', rely='0.05', x='0', y='0')
        self.lbl_dosage = tk.Label(self.frame6)
        self.lbl_dosage.configure(text='Dosage')
        self.lbl_dosage.place(anchor='nw', relx='0.05', rely='0.11', x='0', y='0')
        self.entry_dosage = tk.Entry(self.frame6)
        self.entry_dosage.place(anchor='nw', height='25', relx='0.15', rely='0.11', x='0', y='0')
        self.lbl_diagnosis = tk.Label(self.frame6)
        self.lbl_diagnosis.configure(text='Diagnosis')
        self.lbl_diagnosis.place(anchor='nw', relx='0.05', rely='0.15', x='0', y='0')
        self.btn_create_multi_prescriptions = tk.Button(self.frame6)
        self.btn_create_multi_prescriptions.configure(text='Create')
        self.btn_create_multi_prescriptions.place(anchor='nw', height='34', relx='0.15', rely='0.57', width='80', x='0', y='0')
        self.btn_create_multi_prescriptions.bind('<1>', self.create_multi_prescriptions, add='')
        self.entry_diagnosis = tk.Entry(self.frame6)
        self.entry_diagnosis.place(anchor='nw', height='50', relx='0.15', rely='0.15', width='650', x='0', y='0')
        self.btn_evaluation = tk.Button(self.frame6)
        self.btn_evaluation.configure(text='Evaluation')
        self.btn_evaluation.place(anchor='nw', height='34', relx='0.35', rely='0.57', width='80', x='0', y='0')
        self.btn_evaluation.bind('<1>', self.evaluation, add='')
        self.btn_clear_eval = tk.Button(self.frame6)
        self.btn_clear_eval.configure(text='Clear Evaluations')
        self.btn_clear_eval.place(anchor='nw', height='34', relx='0.55', rely='0.57', width='100', x='0', y='0')
        self.btn_clear_eval.bind('<1>', self.clear_evaluations, add='')
        self.separator1 = ttk.Separator(self.frame6)
        self.separator1.configure(orient='horizontal')
        self.separator1.place(anchor='nw', relx='0.05', rely='0.29', width='720', x='0', y='0')
        self.label1 = ttk.Label(self.frame6)
        self.label1.configure(text='Random')
        self.label1.place(anchor='nw', relx='0.50', rely='0.30', x='0', y='0')
        self.entry_amount = ttk.Entry(self.frame6)
        self.entry_amount.place(anchor='nw', height='25', relx='0.15', rely='0.34', x='0', y='0')
        self.entry_min_diagnosis = ttk.Entry(self.frame6)
        _text_ = '''400'''
        self.entry_min_diagnosis.delete('0', 'end')
        self.entry_min_diagnosis.insert('0', _text_)
        self.entry_min_diagnosis.place(anchor='nw', height='35', relx='0.15', rely='0.44', x='0', y='0')
        self.label2 = ttk.Label(self.frame6)
        self.label2.configure(text='Num. of \nPrescriptions')
        self.label2.place(anchor='nw', relx='0.04', rely='0.33', x='0', y='0')
        self.entry_max_diagnosis = ttk.Entry(self.frame6)
        _text_ = '''4300'''
        self.entry_max_diagnosis.delete('0', 'end')
        self.entry_max_diagnosis.insert('0', _text_)
        self.entry_max_diagnosis.place(anchor='nw', height='35', relx='0.49', rely='0.44', x='0', y='0')
        self.lbl_min = ttk.Label(self.frame6)
        self.lbl_min.configure(text='Min.Diagnosis')
        self.lbl_min.place(anchor='nw', relx='0.04', rely='0.45', x='0', y='0')
        self.lbl_max = ttk.Label(self.frame6)
        self.lbl_max.configure(text='Max.Diagnosis')
        self.lbl_max.place(anchor='nw', relx='0.37', rely='0.45', x='0', y='0')
        self.lbl_char = ttk.Label(self.frame6)
        self.lbl_char.configure(text='\nCharacters:')
        self.lbl_char.place(anchor='nw', relx='0.04', rely='0.39', x='0', y='0')
        self.lbl_max_medication = ttk.Label(self.frame6)
        self.lbl_max_medication.configure(text='Min.Medication')
        self.lbl_max_medication.place(anchor='nw', relx='0.04', rely='0.51', x='0', y='0')
        self.label7 = ttk.Label(self.frame6)
        self.label7.configure(text='Max.Medication')
        self.label7.place(anchor='nw', relx='0.37', rely='0.51', x='0', y='0')
        self.entry_min_medication = ttk.Entry(self.frame6)
        _text_ = '''50'''
        self.entry_min_medication.delete('0', 'end')
        self.entry_min_medication.insert('0', _text_)
        self.entry_min_medication.place(anchor='nw', height='35', relx='0.15', rely='0.50', x='0', y='0')
        self.entry_max_medication = ttk.Entry(self.frame6)
        _text_ = '''200'''
        self.entry_max_medication.delete('0', 'end')
        self.entry_max_medication.insert('0', _text_)
        self.entry_max_medication.place(anchor='nw', height='35', relx='0.49', rely='0.50', x='0', y='0')
        self.btn_single_prescription = ttk.Button(self.frame6)
        self.btn_single_prescription.configure(text='Create This Prescription')
        self.btn_single_prescription.place(anchor='nw', height='34', relx='0.15', rely='0.23', width='135', x='0', y='0')
        self.btn_single_prescription.bind('<1>', self.create_prescription, add='')
        self.btn_info = ttk.Button(self.frame6)
        self.btn_info.configure(text='info')
        self.btn_info.place(anchor='nw', height='25', relx='0.90', rely='0.50', width='30', x='0', y='0')
        self.btn_info.bind('<1>', self.display_amount_of_prescription, add='')
        self.txt_evaluations = tk.Text(self.frame6)
        self.txt_evaluations.configure(blockcursor='false', height='10', width='50')
        self.txt_evaluations.place(anchor='nw', height='200', relx='0.03', rely='0.65', width='740', x='0', y='0')
        self.label11 = ttk.Label(self.frame6)
        self.label11.configure(text='Single')
        self.label11.place(anchor='nw', relx='0.50', rely='0.01', x='0', y='0')
        self.frame6.configure(height='700', width='800')
        self.frame6.pack(side='top')

        # Main widget
        self.mainwindow = self.frame6
    

        
        

    def alert_msg(self,msg):
        tk.messagebox.showinfo(title=None, message=msg)
        
    
    def count_encrypted_prescription_file(self):
        path, dirs, files = next(os.walk("encrypted-prescription-files/"))
        file_count = len(files)
        return file_count
    
    
    def count_prescription_files(self):
        path, dirs, files = next(os.walk("prescriptions-files/"))
        file_count = len(files)
        
        return file_count
    
    def count_files_in_directory(self,path):
        path, dirs, files = next(os.walk(path))
        file_count = len(files)
        
        return file_count
    
    def statistics(self):
        data = []
        with open(r'report/prescriptions_size_in_bytes.txt') as f:
            for line in f:
                fields = line.split()
                rowdata = map(float, fields)
                data.extend(rowdata)
        
        max_prescription_size = max(data)
        min_prescription_size = min(data)
        average_prescription_size = sum(data)/len(data)
        
        return average_prescription_size,max_prescription_size,min_prescription_size
            
        
        
    def display_amount_of_prescription(self,event=None):
        #display_text_file_size = tk.StringVar()
        count = self.count_prescription_files()
        
        self.alert_msg(f"Total of prescriptions: {count}")
        
        
    
    def create_prescription(self, event=None):
    
        file_count = self.count_prescription_files()
        file_count = file_count + 1
        
        diagnosis = self.entry_diagnosis.get()
        medication = self.entry_medication.get()
        dosage = self.entry_dosage.get()
        if(create_prescription_file(file_count,diagnosis,medication,dosage)):
            self.alert_msg("Sucess")
            
            self.display_amount_of_prescription()
           
         
            
        
        else:
            self.alert_msg("Fail in create the prescription")


        return



    def create_multi_prescriptions(self, event=None):
        
        if(self.entry_amount.get()=="" or self.entry_amount.get()=="0" ):
            self.alert_msg("Invalid number of prescriptions")
        
        #self.alert_msg("wait...")
        try:
            #number of prescription to analyse
            number_prescriptions = 0
            number_prescriptions = int(self.entry_amount.get())
            print(number_prescriptions)
    
            #loop for create prescription
            #get the number of prescription previouly created and append
            i_start = self.count_prescription_files()
            for i in range (i_start,i_start+number_prescriptions):
                dosage_size = randint(1,2)
              
                
                min_medication = int(self.entry_min_medication.get())
                max_medication = int(self.entry_max_medication.get())
                
                min_diagnosis = int(self.entry_min_diagnosis.get())
                max_diagnosis = int(self.entry_max_diagnosis.get())
                

                
                medication_size = randint(min_medication,max_medication)
                diagnosis_size = randint(min_diagnosis,max_diagnosis)
                
                print(medication_size)
                print(diagnosis_size)
                
                create_multi_prescriptions_file(i,diagnosis_size,medication_size,dosage_size)
                
            self.alert_msg("Sucess") 

            self.display_amount_of_prescription()
        except:
            
            self.alert_msg("Fail in creation")
            




    def evaluation(self, event=None):
        
        
        if(self.count_prescription_files() == 0):
            self.alert_msg("No prescription")
        else:
            self.alert_msg("Wait...")
            #self.alert_msg("wait...")
            try:
                path, dirs, files = next(os.walk("prescriptions-files/"))
                file_count = len(files)
                number_prescriptions = file_count
                for i in range (0,number_prescriptions):
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
    
               
                self.alert_msg("Evaluations completed !")
               
                
            
            except:
                    self.alert_msg("Fail in evaluation!")
                    
                    
            self.txt_evaluations.insert(tk.END, f"\n\nNumber of Prescriptions Evaluated: {self.count_prescription_files()}")
            self.txt_evaluations.insert(tk.END, f"\nNumber of Prescriptions Encrypted: {self.count_encrypted_prescription_file()}")

            self.txt_evaluations.insert(tk.END, f"\nAverage of prescriptions file size (in bytes): {self.statistics()[0]}")    
            self.txt_evaluations.insert(tk.END, f"\nMax prescription file size (in bytes): {self.statistics()[1]}")    
            self.txt_evaluations.insert(tk.END, f"\nMin prescription file size (in bytes): {self.statistics()[2]}") 
            
    def clear_evaluations(self, event=None):
        if(self.count_prescription_files()==0):
            self.alert_msg("No prescription")
        else:
            
            try:
                
                dir = os.getcwd() + '/prescriptions-files/'
                for f in os.listdir(dir):
                    os.remove(os.path.join(dir, f))
                
                os.remove('report/prescriptions_size_in_bytes.txt') 
                os.remove('report/encripted_prescriptions_size_in_bytes.txt') 
        
                dir = os.getcwd() + '/report/memory-evaluation/'
                for f in os.listdir(dir):
                    os.remove(os.path.join(dir, f))
                
                dir = os.getcwd() + '/report/execution-time-evaluation/'
                for f in os.listdir(dir):
                    os.remove(os.path.join(dir, f))
        
                dir = os.getcwd() + '/encrypted-prescription-files/'
                for f in os.listdir(dir):
                    os.remove(os.path.join(dir, f))
        
                
        
                
                self.alert_msg("Evaluations reseted !!!")
                
                
                
            except:
                   self.alert_msg("Fail to delete files !!!")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = FrontendApp(root)
    app.run()

