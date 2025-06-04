'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.5.1
Descripción:  En un edificio hay dos elevadores (A y B) en distintos pisos. Un usuario llama al elevador
desde un piso p. El elevador más cercano responde, pero si ambos están a la misma
distancia, elige el A.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''


a = int(input("Ingrese el piso donde está el elevador A: "))
b = int(input("Ingrese el piso donde está el elevador B: "))
p = int(input("Ingrese el piso desde donde se llama al elevador (P): "))

# Cálculo de distancias
distA = abs(p - a) #Abs para valor absoluto
distB = abs(p - b)

# Decisión
if distA < distB:
    print("Elevador A")
elif distB < distA:
    print("Elevador B")
else:
    print("Elevador A")  # Si están a la misma distancia, se elige A
