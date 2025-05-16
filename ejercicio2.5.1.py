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
