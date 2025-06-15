'''
Clase:        Clase 10
Tema:         Uso de Matrices
Ejercicio:    10.3.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-14
Estado:       Terminado 
'''

# Pedimos al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz (N): "))

matriz = []

print("Ingrese las filas de la matriz (números separados por coma):")
for i in range(n):
    fila = input(f"Fila {i+1}: ")
    numeros = list(map(int, fila.split(',')))
    matriz.append(numeros)

es_simetrica = True 

for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break 
    if not es_simetrica:
        break

if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")