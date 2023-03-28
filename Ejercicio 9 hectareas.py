print("---Introduce el tipo de conversión---")
print("1. Hectareas")
type_operacion = (input(''))
if type_operacion == '1': 
    hec_m = float(10000)
    hec_km = float(0.01)
    hec_acr = float(2.47105)
    hec_mi = float(0.00386102)
    hec_tareas = float(143)
    print("---Conversor de Hectareas:---")
    print("---Ingrese el valor en hectareas---")  
    val = (float(input('')))
    print("---¿A que valor desea convertir?---")
    print("1. Metros cuadrados") 
    print("2. Kilometros cuadrados")
    print("3. Acres")
    print("4. Millas cuadradas")
    print("5. Tareas")
    type1 =(input('')) 
    if type1 == '1':
        result = print(val,"hectareas equivalen a ",val * hec_m,"metros cuadrados")
    elif type1 == '2':
        result = print(val,"hectareas equivalen a ",val * hec_km,"km cuadrados")
    elif type1 == '3':
        result = print(val,"hectareas equivalen a ",val * hec_acr,"acres")
    elif type1 == '4':
        result = print(val,"hectareas equivalen a ",val * hec_mi,"millas cuadradas")
    elif type1 == '5':
        result = print(val,"hectareas equivalen a ",val * hec_tareas,"tareas")
    else:
        print("Valor invalido")
else:
    print("Cantidad no válida")
print(result)
