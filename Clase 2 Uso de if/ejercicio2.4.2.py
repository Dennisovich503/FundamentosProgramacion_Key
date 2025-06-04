'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.4.2
Descripción:  Determina si un año es bisiesto, considerando las reglas gregorianas. Para que un año
sea bisiesto, debe cumplir alguna de las siguientes condiciones.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''


anio = int(input("Ingrese un año: "))

if (anio % 400 == 0 and anio % 100 != 0) or (anio % 4 == 0):
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
