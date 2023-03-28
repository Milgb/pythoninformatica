print('\n        ***CONVERSIONES DE UNIDADES DE ALMACENAMIENTO***  ')


opcion=input('\n1. Convertir kilobytes \n2. Convertir megabytes\n3. Convertir gigabytes\n3. Convertir terabytes\
                 \nEscoja la opcion que desea: ')

if opcion == '1':
    print('\n     **CONVERSION DE KILOBYTES**  ')
    opcion_submenu=input('1. A megabytes \n2. A gigabytes\n3. A terabytes\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Megabytes*  ')
        kilobytes=int(input("Ingrese la cantidad de kilobytes a convertir: "))
        megabytes = kilobytes * 0.001
        print(kilobytes,"kilobytes equivale a",megabytes,"megabytes")

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Gigabytes*  ')
        kilobytes=int(input("Ingrese la cantidad de kilobytes a convertir: "))
        gigabytes = kilobytes * 0.000001
        print(kilobytes,"kilobytes equivale a",gigabytes,"gigabytes")

    if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Terabytes*  ')
        kilobytes=int(input("Ingrese la cantidad de kilobytes a convertir: "))
        terabytes = kilobytes * 0.000000001
        print(kilobytes,"kilobytes equivale a",terabytes,"terabytes")

    else: print("La opción escogida no es válida")

    
if opcion == '2':
    print('\n     **CONVERSION DE MEGABYTES**  ')
    opcion_submenu=input('1. A kilobytes \n2. A gigabytes\n3. A terabytes\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Kilobytes*  ')
        megabytes=int(input("Ingrese la cantidad de megabytes a convertir: "))
        kilobytes = megabytes * 1000
        print(megabytes,"megabytes equivale a",kilobytes,"kilobytes")

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Gigabytes*  ')
        megabytes=int(input("Ingrese la cantidad de megabytes a convertir: "))
        gigabytes = megabytes * 0.001
        print(megabytes,"megabytes equivale a",gigabytes,"gigabytes")

    if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Terabytes*  ')
        megabytes=int(input("Ingrese la cantidad de megabytes a convertir: "))
        terabytes = megabytes * 0.000001
        print(megabytes,"megabytes equivale a",terabytes,"terabytes")
    else: print("La opción escogida no es válida")


if opcion == '3':
    print('\n     **CONVERSION DE GIGABYTES**  ')
    opcion_submenu=input('1. A kilobytes \n2. A megabytes\n3. A terabytes\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Kilobytes*  ')
        gigabytes=int(input("Ingrese la cantidad de gigabytes a convertir: "))
        kilobytes = gigabytes * 1000000
        print(gigabytes,"gigabytes equivale a",kilobytes,"kilobytes")

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Megabytes*  ')
        gigabytes=int(input("Ingrese la cantidad de gigabytes a convertir: "))
        megabytes = gigabytes * 1000
        print(gigabytes,"gigabytes equivale a",megabytes,"megabytes")

    if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Terabytes*  ')
        gigabytes=int(input("Ingrese la cantidad de gigabytes a convertir: "))
        terabytes = gigabytes * 0.001
        print(gigabytes,"gigabytes equivale a",terabytes,"terabytes")
    else: print("La opción escogida no es válida")


if opcion == '4':
    print('\n     **CONVERSION DE TERABYTES**  ')
    opcion_submenu=input('1. A kilobytes \n2. A megabytes\n3. A gigabytes\
                 \nEscoja la opcion que desea: ')
    
    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Kilobytes*  ')
        terabytes=int(input("Ingrese la cantidad de terabytes a convertir: "))
        kilobytes = terabytes * 1000000000
        print(terabytes,"terabytes equivale a",kilobytes,"kilobytes")

    if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Megabytes*  ')
        terabytes=int(input("Ingrese la cantidad de terabytes a convertir: "))
        megabytes = terabytes * 1000000
        print(terabytes,"terabytes equivale a",megabytes,"megabytes")

    if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a Gigabytes*  ')
        terabytes=int(input("Ingrese la cantidad de terabytes a convertir: "))
        gigabytes = terabytes * 1000
        print(terabytes,"terabytes equivale a",gigabytes,"gigabytes")
    else: print("La opción escogida no es válida")

else: print("La opción escogida no es válida")

        
   



















        
