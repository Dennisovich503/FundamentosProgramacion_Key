

'''
Clase:        Clase 5
Tema:         Uso de listas
Ejercicio:    5.4.2
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-31
Estado:       Terminado 
'''


numero = int(input("Ingresa un número entero entre 1 y 10^9: "))

if 1 <= numero <= 10**9:
    while numero >= 10:
        original = numero
        suma = 0
        print(f"{numero}", end="")
        while numero > 0:
            digito = numero % 10
            suma += digito
            numero = numero // 10
        print(f" = {suma}")
        numero = suma
    print("Resultado final:", numero)
else:
    print("El número debe estar entre 1 y 10^9.")