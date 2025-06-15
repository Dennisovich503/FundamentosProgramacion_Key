n = int(input("Ingrese el número de filas: "))  
m = int(input("Ingrese el número de columnas: ")) 

matriz = []  

print("Ingrese las filas de la matriz (números separados por coma):")
for i in range(n):
    fila_texto = input(f"Fila {i+1}: ")
    numeros = fila_texto.split(",")  
    fila = []  
    for num in numeros:
        fila.append(int(num))  
    matriz.append(fila)  

resultado = []

for i in range(n):
    fila_resultado = []  # Guardará los resultados de una fila
    for j in range(m):
        count = 0  
        for x in [-1, 0, 1]:        
            for y in [-1, 0, 1]:  
                if x == 0 and y == 0:
                    continue
                fila_vecina = i + x
                col_vecina = j + y
                if fila_vecina >= 0 and fila_vecina < n and col_vecina >= 0 and col_vecina < m:
                    if matriz[fila_vecina][col_vecina] == 1:
                        count += 1  

        fila_resultado.append(count)

    resultado.append(fila_resultado) 

print("Matriz con conteo de vecinos con 1:")
for fila in resultado:
    for valor in fila:
        print(valor, end=" ")
    print() 
