from os import system

def file_manager(file='competencia.txt'):
    with open(file,'r') as f:
        print(f.read())
    
