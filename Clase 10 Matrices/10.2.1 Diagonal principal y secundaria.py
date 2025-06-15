'''
Clase:        Clase 10
Tema:         Uso de Matrices
Ejercicio:    10.2.1
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-14
Estado:       Terminado 
'''

# Pedimos al usuario el tamaño de la matriz
t_matriz = int(input("Ingrese el tamaño de la matriz (N): "))

matriz = []

print("Ingrese las filas de la matriz (números separados por coma):")
for i in range(t_matriz):
    fila = input(f"Fila {i+1}: ")
    numeros = list(map(int, fila.split(',')))
    matriz.append(numeros)

# Creamos listas vacías para las diagonales
diagonal_principal = []
diagonal_secundaria = []

# Recorremos la matriz para extraer las diagonales
for i in range(t_matriz):
    diagonal_principal.append(matriz[i][i])              
    diagonal_secundaria.append(matriz[i][t_matriz - 1 - i])    

# Mostramos las listas resultantes
print(diagonal_principal)
print(diagonal_secundaria)
