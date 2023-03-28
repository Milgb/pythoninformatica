print('\n        ***CONVERSIONES DE UNIDADES DE volumen***  ')

opcion=input('\n1. Convertir pies cúbicos \n2. Convertir metros cúbicos\n3. Convertir litros \n4. Convertir mililitros\
                 \nEscoja la opcion que desea: ')

if opcion == '1':
    print('\n     **CONVERSION DE PIES CUBICOS**  ')
    opcion_submenu=input('\n1. A metros cúbicos \n2. A litros\n3. A mililitros\
                 \nEscoja la opcion que desea: ')

    if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a metros cúbicos*  ')
        pies_3=int(input("Ingrese la cantidad de pies cúbicos a convertir: "))
        metros_3 = pies_3 * 0.0283168
        print(pies_3,"pies cúbicos equivalen a",metros_3,"metros cúbicos")

    
    elif opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a litros*  ')
        pies_3=int(input("Ingrese la cantidad de pies cúbicos a convertir: "))
        litros = pies_3 * 28.3168
        print(pies_3,"pies cúbicos equivalen a",litros,"litros")

    elif opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a mililitros*  ')
        pies_3=int(input("Ingrese la cantidad de pies cúbicos a convertir: "))
        mililitros = pies_3 * 28316.8
        print(pies_3,"pies cúbicos equivalen a",mililitros,"mililitros")
        

if opcion == '2':
   print('\n     **CONVERSION DE METROS CUBICOS**  ')
   opcion_submenu=input('\n1. A pies cúbicos \n2. A litros\n3. A mililitros\
                 \nEscoja la opcion que desea: ')

   if opcion_submenu == '1':
    print("--------------------------------------------------------------------------------")
    print('     *Convertir a pies cúbicos*  ')
    metros_3=int(input("Ingrese la cantidad de metros cúbicos a convertir: "))
    pies_3 = metros_3 * 35.3147
    print(metros_3,"metros cúbicos equivalen a",pies_3,"pies cúbicos")

   if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a litros*  ')
        metros_3=int(input("Ingrese la cantidad de metros cúbicos a convertir: "))
        litros = metros_3 * 1000
        print(metros_3,"metros cúbicos equivalen a",litros,"litros")

   if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a mililitros*  ')
        metros_3=int(input("Ingrese la cantidad de metros cúbicos a convertir: "))
        mililitros = metros_3 * 1000000
        print(metros_3,"metros cúbicos equivalen a",mililitros,"mililitros")    


if opcion == '3':
      print('\n     **CONVERSION DE LITROS**  ')
      opcion_submenu=input('\n1. A pies cúbicos \n2. A metros cúbicos\n3. A mililitros\
                 \nEscoja la opcion que desea: ')


      if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a pies cúbicos*  ')
        litros=int(input("Ingrese la cantidad de litros a convertir: "))
        pies_3 = litros * 0.0353147
        print(litros,"litros equivalen a",pies_3,"pies cúbicos")

      if opcion_submenu == '2':  
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a metros cúbicos*  ')
        litros=int(input("Ingrese la cantidad de litros a convertir: "))
        metros_3 = litros * 0.001
        print(litros,"litros equivalen a",metros_3,"pies cúbicos")

      if opcion_submenu == '3':  
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a mililitros*  ')
        litros=int(input("Ingrese la cantidad de litros a convertir: "))
        mililitros = litros * 1000
        print(litros,"litros equivalen a",mililitros,"mililitros")


if opcion == '4':
      print('\n     **CONVERSION DE MILILITROS**  ')
      opcion_submenu=input('\n1. A pies cúbicos \n2. A metros cúbicos\n3. A litros\
                 \nEscoja la opcion que desea: ')
      
      if opcion_submenu == '1':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a pies cúbicos*  ')
        mililitros=int(input("Ingrese la cantidad de mililitros a convertir: "))
        pies_3 = mililitros * 0.00003514997
        print(mililitros,"mililitros equivalen a",pies_3,"pies cúbicos")

      if opcion_submenu == '2':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a metros cúbicos*  ')
        mililitros=int(input("Ingrese la cantidad de mililitros a convertir: "))
        metros_3 = mililitros * 0.000001
        print(mililitros,"mililitros equivalen a",metros_3,"metros cúbicos")

      if opcion_submenu == '3':
        print("--------------------------------------------------------------------------------")
        print('     *Convertir a mililitros*  ')
        mililitros=int(input("Ingrese la cantidad de mililitros a convertir: "))
        litros = mililitros * 0.001
        print(mililitros,"mililitros equivalen a",litros,"litros")






     
      
    
