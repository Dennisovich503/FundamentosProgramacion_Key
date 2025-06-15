'''
Clase:        Clase 10
Tema:         Uso de Matrices
Ejercicio:    10.4.1
Descripción:  Dada una matriz binaria ingresada por el
usuario (0 = agua, 1 = tierra), cuenta la
cantidad de islas disponibles. Una isla está
formada por elementos con valor de 1
conectados horizontal o verticalmente.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-14
Estado:       Terminado 
'''

n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))


print("Ingrese la matriz binaria (cada fila con números separados por coma):")
matriz = []

for i in range(n):
    fila_texto = input(f"Fila {i+1}: ")
    partes_fila = fila_texto.split(",")
    fila = []
    for num in partes_fila:
        fila.append(int(num))
    matriz.append(fila)

visitado = []
for i in range(n):
    fila_visitado = []
    for j in range(m):
        fila_visitado.append(False)
    visitado.append(fila_visitado)

def explorar(i, j):
    pila = [(i, j)] 

    while len(pila) > 0:
        x, y = pila.pop()

        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        if visitado[x][y] or matriz[x][y] == 0:
            continue

        visitado[x][y] = True

        pila.append((x - 1, y))
        pila.append((x + 1, y))  
        pila.append((x, y - 1))  
        pila.append((x, y + 1))  

total_islas = 0

for i in range(n):
    for j in range(m):
        if matriz[i][j] == 1 and not visitado[i][j]:
            total_islas += 1
            explorar(i, j)  

print(total_islas)