anio = int(input("Ingrese un año: "))

if (anio % 400 == 0 and anio % 100 != 0) or (anio % 4 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
