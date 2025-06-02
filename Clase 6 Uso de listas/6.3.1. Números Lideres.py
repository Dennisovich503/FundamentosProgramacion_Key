'''
Clase:        Clase 5
Tema:         Uso de listas
Ejercicio:    6.3.1
Descripción:  Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-30
Estado:       Terminado 
'''



# Ingreso de datos
datos = input("Ingresa los números separados por espacio: ")


numeros = list(map(int, datos.split()))

lideres = []

# Comenzamos desde el final de la lista
maximo = -1
for i in range(len(numeros) - 2, -1, -1):
    if numeros[i] > maximo:
        lideres.append(numeros[i])
        maximo = numeros[i]

lideres.reverse()

for l in lideres:
    print(l, end=" ")

