x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

#Primera zona
zona1 = (x > 0) and (y > 0)

#Segunda zona
zona2 = (x * x + y * y) <= 25

# Evaluar si está en alguna zona peligrosa
if zona1 or zona2:
    print("Peligro")
else:
    print("Seguro")
