print("---Introduce el tipo de conversión---")
print("1. Área")
type_operacion = (input(''))

if type_operacion == '1':
    print("---Conversor de Area---")
    m_cm = float(10000)
    m_dm = float(100)
    m_km = float(0.000001)
    m_pulg = float(1550.0031)
    m_pies = float(10.7639)
    m_hec = float(0.0001)
    m_acr = float(0.000247105)
    m_mill = float(0.000000386102)
    cm_m = float(0.0001)
    cm_dm = float(0.01)
    cm_km = float(0.0000000001)
    cm_pulg = float(0.155)
    cm_pies = float(0.001076)
    cm_hec = float(0.00000001)
    cm_acr = float(0.0000000247105)
    cm_mill = float(0.0000000000386102)
    dm_m = float(0.01)
    dm_cm = float(100)
    dm_km = float(0.00000001)
    dm_pulg = float(15.5)
    dm_pies = float(0.107639)
    dm_hec = float(0.000001)
    dm_acr = float(0.00000247105)
    dm_mill = float(0.00000000386102)
    km_m = float(1000000)
    km_cm = float(100000000000)
    km_dm = float(100000000)
    km_pulg = float(1550003100)
    km_pies = float(10763910.4)
    km_hec = float(10000)
    km_acr = float(247.105)
    km_mill = float(0.386102)
    pulg_m = float(0.00064516)
    pulg_cm = float(6.4516)
    pulg_dm = float(0.064516)
    pulg_km = float(0.00000000064516)
    pulg_pies = float(0.00694444)
    pulg_hec = float(0.000000064516)
    pulg_acr = float(0.0000001594225)
    pulg_mill = float(0.0000000002490975)
    pies_m = float(0.092903)
    pies_cm = float(929.03)
    pies_dm = float(9.2903)
    pies_km = float(0.000000092903)
    pies_pulg = float(144)
    pies_hec = float(0.0000092903)
    pies_acr = float(0.0000229568)
    pies_mill = float(0.0000000358701)
    hec_m = float(10000)
    hec_cm = float(100000000000)
    hec_dm = float(100000000)
    hec_km = float(0.01)
    hec_pulg = float(15500031)
    hec_pies = float(107639.104)
    hec_acr = float(2.47105)
    hec_mill = float(0.00386102)
    acr_m = float(4046.86)
    acr_cm = float(40468600)
    acr_dm = float(404686)
    acr_km = float(0.00404686)
    acr_pulg = float(6272640)
    acr_pies = float(43560)
    acr_hec = float(0.404686)
    acr_mill = float(0.0015625)
    mill_m = float(2589988.11)
    mill_cm = float(2589988110336)
    mill_dm = float(25899881103.36)
    mill_km = float(2.589988)
    mill_pulg = float(4014489600)
    mill_pies = float(27878400)
    mill_hec = float(258.998811)
    mill_acr = float(640)
    print("---Ingrese que unidad desea convertir---")
    print("1. Metros cuadrados")
    print("2. Centimetros cuadrados")
    print("3. Decimetros cuadrados")
    print("4. Kilometros cuadrados")
    print("5. Pulgadas cuadradas")
    print("6. Pies cuadrados")
    print("7. Hectareas")
    print("8. Acres")
    print("9. Millas cuadradas")
    type1 = (input(''))
    print("---Ingrese el valor de la unidad a convertir---")
    val = (float(input('')))
    if type1 == '1':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Centimetros cuadrados")
        print("2. Decimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * m_cm)
        elif type2 == '2':
            result = (val * m_dm)
        elif type2 == '3':
            result = (val * m_km)
        elif type2 == '4':
            result = (val * m_pulg)
        elif type2 == '5':
            result = (val * m_pies)
        elif type2 == '6':
            result = (val * m_hec)
        elif type2 == '7':
            result = (val * m_acr)
        elif type2 == '8':
            result = (val * m_mill)
        else:
            print("Valor invalido")
    elif type1 == '2':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Decimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * cm_m)
        elif type2 == '2':
            result = (val * cm_dm)
        elif type2 == '3':
            result = (val * cm_km)
        elif type2 == '4':
            result = (val * cm_pulg)
        elif type2 == '5':
            result = (val * cm_pies)
        elif type2 == '6':
            result = (val * cm_hec)
        elif type2 == '7':
            result = (val * cm_acr)
        elif type2 == '8':
            result = (val * cm_mill)
        else:
            print("Valor invalido")
    elif type1 == '3':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Kilometros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * dm_m)
        elif type2 == '2':
            result = (val * dm_cm)
        elif type2 == '3':
            result = (val * dm_km)
        elif type2 == '4':
            result = (val * dm_pulg)
        elif type2 == '5':
            result = (val * dm_pies)
        elif type2 == '6':
            result = (val * dm_hec)
        elif type2 == '7':
            result = (val * dm_acr)
        elif type2 == '8':
            result = (val * dm_mill)
        else:
            print("Valor invalido")
    elif type1 == '4':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Pulgadas cuadradas")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * km_m)
        elif type2 == '2':
            result = (val * km_cm)
        elif type2 == '3':
            result = (val * km_dm)
        elif type2 == '4':
            result = (val * km_pulg)
        elif type2 == '5':
            result = (val * km_pies)
        elif type2 == '6':
            result = (val * km_hec)
        elif type2 == '7':
            result = (val * km_acr)
        elif type2 == '8':
            result = (val * km_mill)
        else:
            print("Valor invalido")
    elif type1 == '5':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pies cuadrados")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * pulg_m)
        elif type2 == '2':
            result = (val * pulg_cm)
        elif type2 == '3':
            result = (val * pulg_dm)
        elif type2 == '4':
            result = (val * pulg_km)
        elif type2 == '5':
            result = (val * pulg_pies)
        elif type2 == '6':
            result = (val * pulg_hec)
        elif type2 == '7':
            result = (val * pulg_acr)
        elif type2 == '8':
            result = (val * pulg_mill)
        else:
            print("Valor invalido")
    elif type1 == '6':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Hectareas")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * pies_m)
        elif type2 == '2':
            result = (val * pies_cm)
        elif type2 == '3':
            result = (val * pies_dm)
        elif type2 == '4':
            result = (val * pies_km)
        elif type2 == '5':
            result = (val * pies_pulg)
        elif type2 == '6':
            result = (val * pies_hec)
        elif type2 == '7':
            result = (val * pies_acr)
        elif type2 == '8':
            result = (val * pies_mill)
        else:
            print("Valor invalido")
    elif type1 == '7':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Acres")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * hec_m)
        elif type2 == '2':
            result = (val * hec_cm)
        elif type2 == '3':
            result = (val * hec_dm)
        elif type2 == '4':
            result = (val * hec_km)
        elif type2 == '5':
            result = (val * hec_pulg)
        elif type2 == '6':
            result = (val * hec_pies)
        elif type2 == '7':
            result = (val * hec_acr)
        elif type2 == '8':
            result = (val * hec_mill)
        else:
            print("Valor invalido")
    elif type1 == '8':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Hectareas")
        print("8. Millas cuadradas")
        type2 = (input(''))
        if type2 == '1':
            result = (val * acr_m)
        elif type2 == '2':
            result = (val * acr_cm)
        elif type2 == '3':
            result = (val * acr_dm)
        elif type2 == '4':
            result = (val * acr_km)
        elif type2 == '5':
            result = (val * acr_pulg)
        elif type2 == '6':
            result = (val * acr_pies)
        elif type2 == '7':
            result = (val * acr_hec)
        elif type2 == '8':
            result = (val * acr_mill)
        else:
            print("Valor invalido")
    elif type1 == '9':
        print("---¿A qué valor desea convertirlo?---")
        print("1. Metros cuadrados")
        print("2. Centimetros cuadrados")
        print("3. Decimetros cuadrados")
        print("4. Kilometros cuadrados")
        print("5. Pulgadas cuadradas")
        print("6. Pies cuadrados")
        print("7. Hectareas")
        print("8. Acres")
        type2 = (input(''))
        if type2 == '1':
            result = (val * mill_m)
        elif type2 == '2':
            result = (val * mill_cm)
        elif type2 == '3':
            result = (val * mill_dm)
        elif type2 == '4':
            result = (val * mill_km)
        elif type2 == '5':
            result = (val * mill_pulg)
        elif type2 == '6':
            result = (val * mill_pies)
        elif type2 == '7':
            result = (val * mill_hec)
        elif type2 == '8':
            result = (val * mill_acr)
        else:
            print("Valor invalido")
    else: 
        print("Valor invalido")

print(result)
