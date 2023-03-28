print("Convertidor de masa")
print("1 - kilogramos a gramos \n2 - tonelada a kilogramo\n3 - kilogramo a libra\n4 - kilogramo a onza\n5 - gramo a kilogramo\n6 - libra  a onza\n7 - tonelada larga a tonelada corta\n8 - gramo a miligramo\n9 -miligramo a microgramo \n10 - tonelada larga a tonelada")
opcion = float(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = float(0)
 
if opcion == 1:
    print("kilogramo a gramo")
    entrada = float(input("Ingresa la cantidad en kilogramos: "))
    resultado = float(entrada*1000 )
elif opcion == 2:
    print("toneladas a kilogramos")
    entrada = float(input("Ingresa la cantidad en tonelada: "))
    resultado = float(entrada*1000)
elif opcion == 3:
    print("kilogramo a libra")
    entrada = float(input("Ingresa la cantidad en kilogramo: "))
    resultado = float(entrada*2.205)
elif opcion == 4:
    print("kilogramo a onza")
    entrada = float(input("Ingresa la cantidad en kilogramo: "))
    resultado = float(entrada*35.274)
elif opcion == 5:
    print("gramo a kilogramo")
    entrada = float(input("Ingresa la cantidad en gramo: "))
    resultado = float(entrada/1000)
elif opcion == 6:
    print("libra a onza")
    entrada = float(input("Ingresa la cantidad en libra: "))
    resultado = float(entrada*16)
elif opcion == 7:
    print("tonelada larga a tonelada corta")
    entrada = float(input("Ingresa la cantidad en tonelada larga: "))
    resultado = float(entrada*1.12 )
elif opcion == 8:
    print("gramo a miligramo")
    entrada = float(input("Ingresa la cantidad en gramo: "))
    resultado = float(entrada*1000)
elif opcion == 9:
    print("miligramo a microgramo")
    entrada = float(input("Ingresa la cantidad en centimetros: "))
    resultado = float(entrada*1000 )
elif opcion == 10:
    print("tonelada larga a tonelada ")
    entrada = float(input("Ingresa la cantidad en tonelada larga: "))
    resultado = float(entrada*1.016 )

 
print("El resultado de la conversión es: {0:.2f} ".format(resultado))
