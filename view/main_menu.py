from os import system
from controllers.file_manager import file_manager

def main_menu():

    option = ''
    while option != '0':
        system('cls')
        print('\n\nProyecto 1 - Electiva Programacion con Python')
        print('Elaborado por: Santiago Figueroa')
        print('1.- Archivo')
        print('2.- Acciones')
        print('0.- Salir')

        option = input('Ingrese una opcion: ')
        if option == '1':
            file_manager()
        elif option == '2':
            print('Acciones')
        elif option == '0':
            print('Saliendo...')
        else:
            print('Opcion no valida')
            system('pause')



if __name__ == '__main__':
    main_menu()
