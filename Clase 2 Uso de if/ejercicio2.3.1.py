'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.3.1
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''
contra = input('Ingresa la contraseña: ')

mayusculas = 0
numeros = 0

for letra in contra:
    if letra.isupper():
        mayusculas += 1      
    if letra.isdigit():
        numeros += 1

if len(contra) >= 8 and numeros > 0 and mayusculas > 2:
    print('Contraseña segura')
else:
    print('Contraseña no segura')