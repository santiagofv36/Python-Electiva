from os import system
 # Importo el modulo creado por mi para poder usar la clase Person
from data.person import Person

'''
Esta funcion lee un archivo y guarda los datos en una lista de personas
toma como parametro el nombre del archivo y una lista que puede estar vacia o no
el parametro file es opcional, si no se ingresa un nombre de archivo, se carga uno por defecto
'''

def file_manager(people,file):
    # Si no se ingresa un nombre de archivo, se carga uno por defecto
    
    if file == '':
        file = 'competencia.txt'

    try:
        with open(file,'r') as f:
            lines  = f.readlines()

            for line in lines:
                separated = line.split(',') # Separo por comas el contenido de cada linea, para guardar cada dato en una lista
                # Se crea una persona por cada linea del archivo
                # Para los valores como la edad, horas, minutos y segundos, se convierten a int y los segundos se les elimina el salto de linea

                person = Person(separated[0],separated[1],separated[2],separated[3],separated[4],
                separated[5],int(separated[6]),int(separated[7]),int(separated[8]),int(separated[9].replace('\n',''))) 

                people.append(person)
        # Devuelve la lista de personas
        return people
    except FileNotFoundError as e:
        # TODO: Crear propia excepcion que no existe el archivo
        print('No existe el archivo')

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
        
            
    
