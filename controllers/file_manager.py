from os import system
 # Importo el modulo creado por mi para poder usar la clase Person
from data.person import Person

from datetime import time
from exceptions.IncompleteFile import IncompleteFile
from exceptions.IncosistentValue import IncosistentValue
from exceptions.NotTxt import NotTxt
from exceptions.UnkownFile import UnkownFile

'''
Esta funcion lee un archivo y guarda los datos en una lista de personas
toma como parametro el nombre del archivo y una lista que puede estar vacia o no
el parametro file es opcional, si no se ingresa un nombre de archivo, se carga uno por defecto
'''

def file_manager(people,file):
    # Si no se ingresa un nombre de archivo, se carga uno por defecto
    
    if file == '':
        file = 'competencia.txt'
    elif file.endswith('.txt') == False:
        print(NotTxt(file))
        return

    try:
        with open(file,'r') as f:
            lines  = f.readlines()

            for line in lines:
                separated = line.split(',') # Separo por comas el contenido de cada linea, para guardar cada dato en una lista
                if len(separated) != 10: # Si la lista no tiene 10 elementos, es porque no es el formato correcto por linea
                    print(IncompleteFile(file))
                    break
                # Se crea una persona por cada linea del archivo
                # Para los valores como la edad, horas, minutos y segundos, se convierten a int y los segundos se les elimina el salto de linea
                par_time = time(int(separated[7]),int(separated[8]),int(separated[9].replace('\n','')))
                person = Person(separated[0],separated[1].capitalize(),separated[2].capitalize(),separated[3].capitalize(),separated[4],
                separated[5],int(separated[6]),par_time)
                # Si ya existe la cedula en el sistema no se agrega la persona
                if person.get_id() not in [ person.get_id() for person in people ]:
                    people.append(person)

        # Devuelve la lista de personas
        return people
    except FileNotFoundError as e:
        print(UnkownFile(file))

    except ValueError as ve:
        print(IncosistentValue(file))

# Manejo del menu de archivos

def file_main_menu(people):
    option = ''
    
    # Ciclo hasta que la opcion sea 0

    while option != '0':
        print('1.- Cargar archivo')
        print('0.- Volver al menu principal')
        option = input('Ingrese una opcion: ')
        if option == '1':
            system('cls')
            print('Si no se elige ningun archivo carga uno por defecto')
            file = input('Ingrese el nombre del archivo: ')
            return file_manager(people,file) # Cuando decida cargar un archivo retorno la lista de personas con los datos del archivo

        elif option == '0':
            system('cls')
            print('Volviendo...')
        else:
            system('cls')
            print('Opcion no valida')
            system('pause')
        
            
    
