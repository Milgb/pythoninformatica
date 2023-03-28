
print("Convertidor de monedas")
print("1 - USD a Euro\n2 - USD a peso colombiano\n3 - USD a lempira\n4 - USD a Peso argentino\n5 - USD a Riyal\n6 - USD a Quetzal\n7 - USD a Libra Esterlina\n8 - USD a peso chileno\n9 -USD a peso cubano \n10 - USD a Bolívar")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("USD a Euro")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.93348)
elif opcion == 2:
    print("USD a peso colombiano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*4,817.11)
elif opcion == 3:
    print("USD a lempira")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*24.66)
elif opcion == 4:
    print("USD a peso argentino")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*204.53 )
elif opcion == 5:
    print("USD a Riyal")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*3.64)
elif opcion == 6:
    print("USD a Quetzal")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*7.80)
elif opcion == 7:
    print("USD a Libra Esterlina")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*0.81 )
elif opcion == 8:
    print("USD a peso chileno")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*826.08)
elif opcion == 9:
    print("USD a peso cubano")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*24.00 )
elif opcion == 10:
    print("USD a Bolívar")
    entrada = float(input("Ingresa la cantidad en USD: "))
    resultado = float(entrada*24.10 )

 
print("El resultado de la conversión es: {0:.2f} ".format(resultado))

