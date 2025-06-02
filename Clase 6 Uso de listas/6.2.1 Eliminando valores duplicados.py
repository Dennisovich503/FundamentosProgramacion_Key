'''
Clase:        Clase 6
Tema:         Uso de listas
Ejercicio:    6.2.1
Descripción:  Cree un programa que elimine los números repetidos de una lista

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-30
Estado:       Terminado 
'''

#Versión1
numeros = input('Ingresa una lista de números(separa por espacio): ')
    
no_repetidos = []

for n in numeros:
    if n not in no_repetidos:
        no_repetidos.append(n)
    else:
        no_repetidos.append('')
        

print('Lista con números repetidos:', end=' ')
for n in numeros:
    print(n, end='')

print('\nLista de números sin repetir:', end=' ')
for n in no_repetidos:
    print(n, end='')



'''
numeros = []
while True:
    num = int(input('Ingresa el número: '))
    numeros.append(num)
    conf = input('¿Deseas seguir ingresando números? si/no: ')
    if(conf == 'no'):
        break
    else:
        pass
    
no_repetidos = []

for n in numeros:
    if n not in no_repetidos:
        no_repetidos.append(n)
        

print('Lista con números repetidos:', end=' ')
for n in numeros:
    print(n, end=' ')

print('\nLista de números sin repetir:', end=' ')
for n in no_repetidos:
    print(n, end=' ')
'''   
    
    
    