print('\n        ***CONVERSIONES DE UNIDADES DE TIEMPO***  ')

opcion=input('\n1. Convertir horas \n2. Convertir minutos\n3. Convertir segundos\
                 \nEscoja la opcion que desea: ')

if opcion == '1':
    print('\n     **CONVERSION DE HORAS**  ')
    opcion_submenu=input('1. A minutos \n2. A segundos\
                 \nEscoja la opcion que desea: ')
    
    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a minutos*  ')
        horas=int(input("Ingrese la cantidad de horas a convertir: "))
        minutos = horas * 60
        print(horas,"hora equivale a",minutos,"minutos") 

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a segundos*  ')
        horas=int(input("Ingrese la cantidad de horas a convertir: "))
        segundos = horas * 3600
        print(horas,"hora equivale a",segundos,"segundos")


if opcion == '2':
    print('\n     **CONVERSION DE MINUTOS**  ')
    opcion_submenu=input('1. A horas \n2. A segundos\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a horas*  ')
        minutos=int(input("Ingrese la cantidad de minutos a convertir: "))
        horas = minutos /60
        print(minutos,"minutos equivalen a",horas,"horas")

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a segundos*  ')
        minutos=int(input("Ingrese la cantidad de horas a convertir: "))
        segundos = minutos * 60
        print(minutos,"minutos equivale a",segundos,"segundos")

if opcion == '3':
    print('\n     **CONVERSION DE SEGUNDOS**  ')
    opcion_submenu=input('1. A horas \n2. A minutos\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1': 
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a horas*  ')
        segundos=int(input("Ingrese la cantidad de segundos a convertir: "))
        horas = segundos /3600
        print(segundos,"segundos equivalen a",horas,"horas")

    if opcion_submenu == '2': 
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a minutos*  ')
        segundos=int(input("Ingrese la cantidad de segundos a convertir: "))
        minutos = segundos /60
        print(segundos,"segundos equivalen a",minutos,"minutos")


        







        


