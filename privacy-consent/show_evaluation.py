from colors import *
from filestatistics import *

def show_evaluation():

         prescription_info = filestatistics("report/CLEAR_TEXT_prescription_size_in_kb")   
         print("\nPrescription Info")
         print(f"Avg.: {prescription_info[0]} kb ({prescription_info[0]/1024} MB)")
         print(f"Max.: {prescription_info[1]} kb ({prescription_info[1]/1024} MB)")   
         print(f"Min.: {prescription_info[2]} kb ({prescription_info[2]/1024} MB)")  


         personal_id_info = filestatistics("report/CLEAR_TEXT_personal_id_size_in_kb")   
         print("\nPersonal ID Info")
         print(f"Avg.: {personal_id_info[0]} kb ({personal_id_info[0]/1024} MB)")
         print(f"Max.: {personal_id_info[1]} kb ({personal_id_info[1]/1024} MB)")   
         print(f"Min.: {personal_id_info[2]} kb ({prescription_info[2]/1024} MB)")  


         medication_info = filestatistics("report/CLEAR_TEXT_medication_size_in_kb")   
         print("\nMedication Info")
         print(f"Avg.: {medication_info[0]} kb ({medication_info[0]/1024} MB)")
         print(f"Max.: {medication_info[1]} kb ({medication_info[1]/1024} MB)")   
         print(f"Min.: {medication_info[2]} kb ({medication_info[2]/1024} MB)")  


         diagnosis_info = filestatistics("report/CLEAR_TEXT_diagnosis_size_in_kb")   
         print("\nDiagnosis Info")
         print(f"Avg.: {diagnosis_info[0]} kb ({diagnosis_info[0]/1024} MB)")
         print(f"Max.: {diagnosis_info[1]} kb ({diagnosis_info[1]/1024} MB)")   
         print(f"Min.: {diagnosis_info[2]} kb ({diagnosis_info[2]/1024} MB)")  


         print(f"{bcolors.WARNING}\n#################### Encryption #############################{bcolors.ENDC}")

         print("\nMemory Allocation (kb):")


         memory_evaluation_personal_ID = filestatistics("report/memory-evaluation/PERSONAL_ID_encryption_memory_usage_in_kb.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {memory_evaluation_personal_ID[0]} kb")
         print(f"Max.: {memory_evaluation_personal_ID[1]} kb")   
         print(f"Min.: {memory_evaluation_personal_ID[2]} kb")  


         memory_evaluation_medication = filestatistics("report/memory-evaluation/MEDICATION_encryption_memory_usage_in_kb.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {memory_evaluation_medication[0] } kb")
         print(f"Max.: {memory_evaluation_medication[1] } kb")   
         print(f"Min.: {memory_evaluation_medication[2] } kb")     



         memory_evaluation_diagnosis = filestatistics("report/memory-evaluation/DIAGNOSIS_encryption_memory_usage_in_kb.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {memory_evaluation_diagnosis[0] } kb")
         print(f"Max.: {memory_evaluation_diagnosis[1] } kb")   
         print(f"Min.: { memory_evaluation_diagnosis[2] } kb")     


        
         print("\nExecution Time (ms):")


         execution_time_personal_ID = filestatistics("report/execution-time-evaluation/PERSONAL_ID_encryption_execution_time_in_ms.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {execution_time_personal_ID[0]} ms")
         print(f"Max.: {execution_time_personal_ID[1]} ms")   
         print(f"Min.: {execution_time_personal_ID[2]} ms")  


         execution_time_medication = filestatistics("report/execution-time-evaluation/MEDICATION_encryption_execution_time_in_ms.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {execution_time_medication[0] } ms")
         print(f"Max.: {execution_time_medication[1] } ms")   
         print(f"Min.: {execution_time_medication[2] } ms")     



         execution_time_diagnosis = filestatistics("report/execution-time-evaluation/DIAGNOSIS_encryption_execution_time_in_ms.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {execution_time_diagnosis[0] } ms")
         print(f"Max.: {execution_time_diagnosis[1] } ms")   
         print(f"Min.: { execution_time_diagnosis[2] } ms")  

         print(f"{bcolors.WARNING}\n#################### END Encryption #############################{bcolors.ENDC}")










         print(f"{bcolors.HEADER}\n#################### Delegation  #############################{bcolors.ENDC}")
         print("\nMemory Allocation (kb):")

         memory_evaluation_personal_ID = filestatistics("report/memory-evaluation/PERSONAL_ID_delegation_memory_usage_in_kb.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {memory_evaluation_personal_ID[0]} kb")
         print(f"Max.: {memory_evaluation_personal_ID[1]} kb")   
         print(f"Min.: {memory_evaluation_personal_ID[2]} kb")  


         memory_evaluation_medication = filestatistics("report/memory-evaluation/MEDICATION_delegation_memory_usage_in_kb.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {memory_evaluation_medication[0] } kb")
         print(f"Max.: {memory_evaluation_medication[1] } kb")   
         print(f"Min.: {memory_evaluation_medication[2] } kb")     



         memory_evaluation_diagnosis = filestatistics("report/memory-evaluation/DIAGNOSIS_delegation_memory_usage_in_kb.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {memory_evaluation_diagnosis[0] } kb")
         print(f"Max.: {memory_evaluation_diagnosis[1] } kb")   
         print(f"Min.: { memory_evaluation_diagnosis[2] } kb")     


        
         print("\nExecution Time (ms):")


         execution_time_personal_ID = filestatistics("report/execution-time-evaluation/PERSONAL_ID_delegation_execution_time_in_ms.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {execution_time_personal_ID[0]} ms")
         print(f"Max.: {execution_time_personal_ID[1]} ms")   
         print(f"Min.: {execution_time_personal_ID[2]} ms")  


         execution_time_medication = filestatistics("report/execution-time-evaluation/MEDICATION_delegation_execution_time_in_ms.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {execution_time_medication[0] } ms")
         print(f"Max.: {execution_time_medication[1] } ms")   
         print(f"Min.: {execution_time_medication[2] } ms")     



         execution_time_diagnosis = filestatistics("report/execution-time-evaluation/DIAGNOSIS_delegation_execution_time_in_ms.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {execution_time_diagnosis[0] } ms")
         print(f"Max.: {execution_time_diagnosis[1] } ms")   
         print(f"Min.: { execution_time_diagnosis[2] } ms")  

         print(f"{bcolors.HEADER}\n#################### END Delegation #############################{bcolors.ENDC}")

    







         print(f"{bcolors.WARNING}\n#################### Re-Encryption #############################{bcolors.ENDC}")

         print("\nMemory Allocation (kb):")


         memory_evaluation_personal_ID = filestatistics("report/memory-evaluation/PERSONAL_ID_reencryption_memory_usage_in_kb.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {memory_evaluation_personal_ID[0]} kb")
         print(f"Max.: {memory_evaluation_personal_ID[1]} kb")   
         print(f"Min.: {memory_evaluation_personal_ID[2]} kb")  


         memory_evaluation_medication = filestatistics("report/memory-evaluation/MEDICATION_reencryption_memory_usage_in_kb.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {memory_evaluation_medication[0] } kb")
         print(f"Max.: {memory_evaluation_medication[1] } kb")   
         print(f"Min.: {memory_evaluation_medication[2] } kb")     



         memory_evaluation_diagnosis = filestatistics("report/memory-evaluation/DIAGNOSIS_reencryption_memory_usage_in_kb.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {memory_evaluation_diagnosis[0] } kb")
         print(f"Max.: {memory_evaluation_diagnosis[1] } kb")   
         print(f"Min.: { memory_evaluation_diagnosis[2] } kb")     


    
         print("\nExecution Time (ms):")


         execution_time_personal_ID = filestatistics("report/execution-time-evaluation/PERSONAL_ID_reencryption_execution_time_in_ms.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {execution_time_personal_ID[0]} ms")
         print(f"Max.: {execution_time_personal_ID[1]} ms")   
         print(f"Min.: {execution_time_personal_ID[2]} ms")  


         execution_time_medication = filestatistics("report/execution-time-evaluation/MEDICATION_reencryption_execution_time_in_ms.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {execution_time_medication[0] } ms")
         print(f"Max.: {execution_time_medication[1] } ms")   
         print(f"Min.: {execution_time_medication[2] } ms")     



         execution_time_diagnosis = filestatistics("report/execution-time-evaluation/DIAGNOSIS_reencryption_execution_time_in_ms.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {execution_time_diagnosis[0] } ms")
         print(f"Max.: {execution_time_diagnosis[1] } ms")   
         print(f"Min.: { execution_time_diagnosis[2] } ms")  

         print(f"{bcolors.WARNING}\n#################### END Re-Encryption #############################{bcolors.ENDC}")











         print(f"{bcolors.OKCYAN}\n#################### Decryption #############################{bcolors.ENDC}")
         print("")
         print("\nMemory Allocation (kb):")

         memory_evaluation_personal_ID = filestatistics("report/memory-evaluation/PERSONAL_ID_decryption_memory_usage_in_kb.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {memory_evaluation_personal_ID[0]} kb")
         print(f"Max.: {memory_evaluation_personal_ID[1]} kb")   
         print(f"Min.: {memory_evaluation_personal_ID[2]} kb")  


         memory_evaluation_medication = filestatistics("report/memory-evaluation/MEDICATION_decryption_memory_usage_in_kb.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {memory_evaluation_medication[0] } kb")
         print(f"Max.: {memory_evaluation_medication[1] } kb")   
         print(f"Min.: {memory_evaluation_medication[2] } kb")     



         memory_evaluation_diagnosis = filestatistics("report/memory-evaluation/DIAGNOSIS_decryption_memory_usage_in_kb.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {memory_evaluation_diagnosis[0] } kb")
         print(f"Max.: {memory_evaluation_diagnosis[1] } kb")   
         print(f"Min.: { memory_evaluation_diagnosis[2] } kb")     


        
         print("\nExecution Time (ms):")


         execution_time_personal_ID = filestatistics("report/execution-time-evaluation/PERSONAL_ID_decryption_execution_time_in_ms.txt") 
         print("\nPersonal ID")
         print(f"Avg.: {execution_time_personal_ID[0]} ms")
         print(f"Max.: {execution_time_personal_ID[1]} ms")   
         print(f"Min.: {execution_time_personal_ID[2]} ms")  


         execution_time_medication = filestatistics("report/execution-time-evaluation/MEDICATION_decryption_execution_time_in_ms.txt") 
         print("\nMedication and Dosage")
         print(f"Avg.: {execution_time_medication[0] } ms")
         print(f"Max.: {execution_time_medication[1] } ms")   
         print(f"Min.: {execution_time_medication[2] } ms")     



         execution_time_diagnosis = filestatistics("report/execution-time-evaluation/DIAGNOSIS_decryption_execution_time_in_ms.txt") 
         print("\nDiagnosis")
         print(f"Avg.: {execution_time_diagnosis[0] } ms")
         print(f"Max.: {execution_time_diagnosis[1] } ms")   
         print(f"Min.: { execution_time_diagnosis[2] } ms")      

         print(f"{bcolors.OKCYAN}\n#################### END Decryption #############################{bcolors.ENDC}")
