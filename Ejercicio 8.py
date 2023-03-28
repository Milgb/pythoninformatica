
num = int(input("Ingrese un numero entero: "))

if num % 3 == 0 and num % 5 == 0:
    print("Es multiplo de 3 y de 5")
elif num % 3 == 0: 
    print("Es multiplo de 3")
elif num % 5 == 0:
    print("Es multiplo de 5")
else:
    print("No es multiplo de 3 ni de 5")

        
