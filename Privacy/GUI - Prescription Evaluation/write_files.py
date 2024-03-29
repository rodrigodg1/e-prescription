#store the sizes in file
from file_operations import *

def write_prescription(path,prescription_file_size):
    with open(path, 'a') as f:
        f.write(str(prescription_file_size))
        f.write("\n")

def write_memory_usage(path,peak):
    peak = peak*0.001
    with open(path, 'a') as f:
        f.write(str(peak))
        f.write("\n")

#receives time in s
def write_execution_time(path,time):
    #convert to ms
    time = time * 1000
    with open(path, 'a') as f:
        f.write(str(time))
        f.write("\n")

#

