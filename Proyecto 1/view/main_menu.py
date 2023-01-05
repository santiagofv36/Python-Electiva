from os import system, name
from controllers.file_manager import file_main_menu
from controllers.actions import main_menu_actions


def main_menu():
    option = ''
    people = [] # Para poder usar la variable people en todos los menus
    while option != '0':
        
        print('\n\nProyecto 1 - Electiva Programacion con Python')
        print('Elaborado por: Santiago Figueroa')
        print('1.- Archivo')
        print('2.- Acciones')
        print('0.- Salir')

        option = input('Ingrese una opcion: ')
        if option == '1':
            if name == 'posix':
                system('clear')
            else:
                system('cls')
            people = file_main_menu(people)
        elif option == '2':
            if name == 'posix':
                system('clear')
            else:
                system('cls')
            print('Acciones')
            main_menu_actions(people)
        elif option == '0':
            if name == 'posix':
                system('clear')
            else:
                system('cls')
            print('Saliendo...')
        else:
            if name == 'posix':
                system('clear')
            else:
                system('cls')
            print('Opcion no valida')
            input('Presione cualquier tecla para continuar')



if __name__ == '__main__':
    main_menu()
