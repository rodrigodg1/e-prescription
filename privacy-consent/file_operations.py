import os

from write_files import *

def open_file(file):
    f = open(file, "r")
    prescription = f.read()
    return prescription

def file_size(file):
    #size = os.path.getsize('f:/file.txt') 
    prescription_file_size = os.path.getsize(file)
    return prescription_file_size

def count_files_in_directory(directory):
    path, dirs, files = next(os.walk(directory))
    file_count = len(files)
    return file_count


def str_to_binary(str):
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary

def binary_to_str(binary):
    jsn = ''.join(chr(int(x, 2)) for x in binary.split())
    return jsn
    
def create_file_with_size(path_to_count,directory,path_destination):
    count_prescription_files = count_files_in_directory(path_to_count)
    for p in range (0,count_prescription_files):
            size = file_size(f"{path_to_count}{directory}{p}")
            write_prescription_size(f"{path_destination}",size)
