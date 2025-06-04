'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.4.1
Descripción:  Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''

numero = int(input('Ingresa el número: '))

if numero%7==0 and numero%5!=0:
    print('¡Es mágico!')
else:
    print('¡No es mágico!')