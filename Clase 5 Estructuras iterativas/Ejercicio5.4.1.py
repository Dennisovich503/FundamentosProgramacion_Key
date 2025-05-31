'''
Clase:        Clase 5
Tema:         Bluces for y while
Ejercicio:    5.4.1
Descripción:  Generar un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
numero fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-31
Estado:       Terminado 
'''

import random

# Generar número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

while True:
    numero = int(input('Ingresa un número entre 1 y 100: '))
        
    if numero < 1 or numero > 100:
        print('Por favor, ingresa un número entre 1 y 100.')
    else:  
        if numero < numero_aleatorio:
            print('El número secreto es mayor.')
        elif numero > numero_aleatorio:
            print('El número secreto es menor.')
        else:
            print(f'¡Felicidades! Has adivinado el número secreto: {numero}')
            break
        
