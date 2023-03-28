print("Convertidor de longitudes")
print("1 - metro a kilometros \n2 - metros a centimetro\n3 - metro a decímetro\n4 - metro a hectrometro\n5 - metro a decametro\n6 - metro a milimetro\n7 - decametro a metro\n8 - kilometros a metros\n9 -centimetros a metros \n10 - milimetros a metros")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("metro a kilometros")
    entrada = float(input("Ingresa la cantidad en metro: "))
    resultado = float(entrada/1000 )
elif opcion == 2:
    print("metros a centimetros")
    entrada = float(input("Ingresa la cantidad en metros: "))
    resultado = float(entrada*100)
elif opcion == 3:
    print("metros a decimetros")
    entrada = float(input("Ingresa la cantidad en metros: "))
    resultado = float(entrada*10)
elif opcion == 4:
    print("metro a hectrometro")
    entrada = float(input("Ingresa la cantidad en metros: "))
    resultado = float(entrada/100)
elif opcion == 5:
    print("metro a decametro")
    entrada = float(input("Ingresa la cantidad en metros: "))
    resultado = float(entrada/10)
elif opcion == 6:
    print("metro a milimetro")
    entrada = float(input("Ingresa la cantidad en metros: "))
    resultado = float(entrada*1000)
elif opcion == 7:
    print("metro a metro")
    entrada = float(input("Ingresa la cantidad en decametro: "))
    resultado = float(entrada*10 )
elif opcion == 8:
    print("kilometros a metros")
    entrada = float(input("Ingresa la cantidad en kilometros: "))
    resultado = float(entrada*1000)
elif opcion == 9:
    print("centimetros a metros")
    entrada = float(input("Ingresa la cantidad en centimetros: "))
    resultado = float(entrada/100 )
elif opcion == 10:
    print("milimetros a metros")
    entrada = float(input("Ingresa la cantidad en milimetros: "))
    resultado = float(entrada/1000 )

 
print("El resultado de la conversión es: {0:.2f} ".format(resultado))

