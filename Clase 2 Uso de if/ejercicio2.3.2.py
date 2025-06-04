'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.3.2
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
tabla.

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''

consumo = int(input('Ingresa las unidades de consumo: '))

if consumo >= 201:
    print(f'Impuesto aplicado: ${consumo * 0.7}')
elif consumo >= 101 and consumo <=200:
    print(f'Impuesto aplicado: ${consumo * 0.5}')
else:
    print('Sin impuestos')