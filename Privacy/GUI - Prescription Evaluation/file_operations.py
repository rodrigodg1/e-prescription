import os

def open_file(name):
    f = open(name, "r")
    prescription = f.read()
    return prescription

def file_size(name):
    prescription_file_size = os.path.getsize(name)
    return prescription_file_size