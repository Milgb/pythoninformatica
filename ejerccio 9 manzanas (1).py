
print("---Introduce el tipo de conversión---")
print("1. Manzanas")
type_operacion = (input(''))
       
if type_operacion == '1':
    man_m = float(6987)
    man_hec = float(0.6987)
    man_acr = float(1.7259)
    man_km = float(0.00006987)
    man_pies = float(75003.89)
    man_pulg = float(10890078.24)
    man_mill = float(0.00002707)
    print("---Convertir Manzanas:---")
    print("---Ingrese la cantidad de manzanas---")
    val = (float(input('')))
    print("---¿A que unidad desea convertir las manzanas---")
    print("1. Metros Cuadrados")
    print("2. Hectáreas")
    print("3. Kilometros cuadrados")
    print("4. Pies cuadrados")
    print("5. Pulgadas cuadradas")
    print("6. Millas cuadradas")
    type1 = (input(''))
    if type1 == '1':
        result = print(val,"manzanas equivalen a ",val * man_m,"metros cuadrados")
    elif type1 == '2':
        result = print(val,"manzanas equivalen a ",val * man_hec, "hectareas")
    elif type1 == '3':
        result = print(val,"manzanas equivalen a ",val * man_km, "km cuadrados")
    elif type1 == '4':
        result = print(val,"manzanas equivalen a ",val * man_pies,"pies cuadrados")
    elif type1 == '5':
        result = print(val,"manzanas equivalen a ",val * man_pulg,"pulgadas cuadradas")
    elif type1 == '6':
        result = print(val,"manzanas equivalen a ",val * man_mill,"millas cuadradas")
    else:
        print("Valor invalido")

print(result)


    
