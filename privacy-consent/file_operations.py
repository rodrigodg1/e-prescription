import os

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