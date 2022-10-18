from os import system

from data.person import Person

def file_manager(file='competenci.txt'):
    try:
        with open(file,'r') as f:
            lines  = f.readlines()
            people = []
            for line in lines:
                separated = line.split(',') # Separo por comas el contenido de cada linea, para guardar cada dato en una lista
                # Se crea una persona por cada linea del archivo

                person = Person(separated[0],separated[1],separated[2],separated[3],separated[4],
                separated[5],int(separated[6]),int(separated[7]),int(separated[8]),int(separated[9].replace('\n','')))
                people.append(person)
    except FileNotFoundError as e:
        # TODO: Crear propia excepcion que no existe el archivo
        system('pause')
        print('No existe el archivo')
        


        
            
    
