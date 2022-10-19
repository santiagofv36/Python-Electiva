from os import system


'''
Funcion que imprime la lista de participantes
Mediante el uso de compresion de listas se obtienen los datos de cada persona y se almacenan en una lista
Luego se inserta la lista de encabezados
Se obtiene la longitud de cada columna
Se crea un formato para imprimir la lista
Se imprime la lista
El codigo que genera la tabla fue sacado de 
https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data Repuesta 14
'''

def print_participants(table):
    
    if len(table) == 0:
        print('No hay participantes')
        return

    list_to_print = [ person.return_list() for person in table ]

    list_to_print.insert(0, ['Cedula', 'Apellido', 'Segundo apellido', 'Nombre', 'Inicial', 'Sexo', 'Edad', 'Horas', 'Minutos', 'Segundos'])

    longest_cols = [max(len(str(row[i])) for row in list_to_print) + 3 for i in range(len(list_to_print[0]))]
    row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
    for row in list_to_print:
        print(row_format.format(*row))


# Funcion que retorna la cantidad total de participantes
def total_participants(people):
    return len(people)



# Metodo que devuelve todos los participantes por grupo etario
def age_group(people):
    
    if len(people) ==0:
        print('No hay participantes')
        return

    juniors = [ person for person in people if person.get_age() <= 25 ]
    seniors = [ person for person in people if person.get_age() > 25 and person.get_age() <= 40 ]
    masters = [ person for person in people if person.get_age() > 40 ]


    return [juniors, seniors, masters]


# Metodo que retorna los participantes por sexo
def sex_group(people):
        
    if len(people) == 0:
        print('No hay participantes')
        return

    hombre = [ person for person in people if person.get_sex() in ['M', 'm'] ]
    mujer = [ person for person in people if person.get_sex() in ['F', 'f'] ]

    return [hombre, mujer]

# Metodo que retorna los ganadores por grupo etario en forma de una lista de personas
def winners_by_age(people):
    
    if len(people) == 0:
        print('No hay participantes')
        return

    junior,senior,master = age_group(people)


    winner_junior = min(junior, key=lambda person: person.get_time())
    winner_senior = min(senior, key=lambda person: person.get_time())
    winner_master = min(master, key=lambda person: person.get_time())

    return [winner_junior, winner_senior, winner_master]


# Metodo que retorna los ganadores por sexo en forma de una lista de personas
def winners_by_sex(people):
        
    if len(people) == 0:
        print('No hay participantes')
        return

    hombre, mujer = sex_group(people)

    winner_hombre = min(hombre, key=lambda person: person.get_time())
    winner_mujer = min(mujer, key=lambda person: person.get_time())

    return [winner_hombre, winner_mujer]

# Metodo que retorna los ganadores por grupo etario y sexo en forma de una lista de personas

def winners_by_age_and_sex(people):
        
        if len(people) == 0:
            print('No hay participantes')
            return
    
        junior,senior,master = age_group(people)
        hombre, mujer = sex_group(people)

        # Se hace una lista que une a los hombres y mujeres con los grupos etarios

        junior_hombre = [ person for person in junior if person in hombre ]
        junior_mujer = [ person for person in junior if person in mujer ]
        senior_hombre = [ person for person in senior if person in hombre ]
        senior_mujer = [ person for person in senior if person in mujer ]
        master_hombre = [ person for person in master if person in hombre ]
        master_mujer = [ person for person in master if person in mujer ]

        # Se obtienen los ganadores de cada grupo etario y sexo

        winner_junior_hombre = min(junior_hombre, key=lambda person: person.get_time())
        winner_junior_mujer = min(junior_mujer, key=lambda person: person.get_time())
        winner_senior_hombre = min(senior_hombre, key=lambda person: person.get_time())
        winner_senior_mujer = min(senior_mujer, key=lambda person: person.get_time())
        winner_master_hombre = min(master_hombre, key=lambda person: person.get_time())
        winner_master_mujer = min(master_mujer, key=lambda person: person.get_time())

        # se retorna la lista de ganadores

        return [winner_junior_hombre, winner_junior_mujer, winner_senior_hombre, winner_senior_mujer, winner_master_hombre, winner_master_mujer]


def winner(people):

    if len(people) == 0:
        print('No hay participantes')
        return

    return min(people, key=lambda person: person.get_time())


def main_menu_actions(people):  
    
    option = ''
    while option != '0':
        
        print('\n\n\n MENU DE ACCIONES\n\n\n')
        print('1.- Lista con total de participantes')
        print('2.- Cantidad total de participantes')
        print('3.- Cantidad de participantes por grupo etario')
        print('4.- Cantidad de participantes por sexo')
        print('5.- Ganadores por grupo etario')
        print('6.- Ganadores por sexo')
        print('7.- Ganadores por grupo etario y sexo')
        print('8.- Ganador General')
        print('9.- Histograma de participante por grupo etario')
        print('10.- Histograma de participante por sexo y grupo etario')
        print('11.- Promedio de tiempo por grupo etario y sexo')

        option = input('Ingrese una opcion: ')
        if option == '1':
            system('cls')
            print('\n\nLista con total de participantes\n\n')
            print_participants(people)
            system('pause')
            system('cls')
        elif option == '2':
            system('cls')
            print('\n\nCantidad total de participantes\n\n')
            print(f'Cantidad de participantes: {total_participants(people)}')
            system('pause')
            system('cls')
        elif option == '3':
            system('cls')
            print('\n\nCantidad de participantes por grupo etario\n\n')
            junior, senior, master = age_group(people)
            if len(people) == 0:
                print('No hay participantes')
            else:
                print('Juniors\t\tSeniors\t\tMasters')
                print(f'{len(junior)}\t\t{len(senior)}\t\t{len(master)}')
            system('pause')
            system('cls')
        elif option == '4':
            system('cls')
            print('\n\nCantidad de participantes por sexo\n\n')
            amount = sex_group(people)
            if len(people) == 0:
                print('No hay participantes')
            else:
                print('Hombres\t\tMujeres')
                print(f'{len(amount[0])}\t\t{len(amount[1])}')
            system('pause')
            system('cls')
        elif option == '5':
            system('cls')
            print('\n\nGanadores por grupo etario\n\n')
            winners = winners_by_age(people)
            if len(people) == 0:
                print('No hay participantes')
            else:
                print('Juniors\t\tSeniors\t\tMasters')
                print(f'{winners[0].get_name()}\t{winners[1].get_name()}\t{winners[2].get_name()}')
            system('pause')
            system('cls')
        elif option == '6':
            system('cls')
            print('\n\nGanadores por sexo\n\n')

            if len(people) == 0:
                print('No hay participantes')
            else:
                winners = winners_by_sex(people)
                print('Hombres\t\tMujeres')
                print(f'{winners[0].get_name()}\t{winners[1].get_name()}')

            system('pause')
            system('cls')
        elif option == '7':
            system('cls')
            print('\n\nGanadores por grupo etario y sexo\n\n')
            if len(people) == 0:
                print('No hay participantes')
            else:
                winners = winners_by_age_and_sex(people)
                print('\t  Juniors  \t\tSeniors  \t\tMasters')
                print(f'Hombres:  {winners[0].get_name()}  \t{winners[2].get_name()}  \t{winners[4].get_name()}')
                print(f'Mujeres:  {winners[1].get_name()}  \t{winners[3].get_name()}  \t{winners[5].get_name()}')
            
            system('pause')
            system('cls')
        elif option == '8':
            system('cls')
            print('\n\nGanador General\n\n')
            if len(people) == 0:
                print('No hay participantes')
            else:
                print(f'Ganador General: {winner(people).get_name()}')
            system('pause')
            system('cls')
        elif option == '9':
            system('cls')
            print('\n\nHistograma de participante por grupo etario\n\n')
            system('cls')
        elif option == '10':
            system('cls')
            print('\n\nHistograma de participante por sexo y grupo etario\n\n')
            system('cls')
        elif option == '11':
            system('cls')
            print('\n\nPromedio de tiempo por grupo etario y sexo\n\n')
            system('cls')
        elif option == '0':
            system('cls')
            print('Volviendo...')
            system('cls')
        else:
            system('cls')
            print('Opcion no valida')
            system('cls')
            system('pause')