consumo = int(input('Ingresa las unidades de consumo: '))

if consumo >= 201:
    print(f'Impuesto aplicado: ${consumo * 0.7}')
elif consumo >= 101 and consumo <=200:
    print(f'Impuesto aplicado: ${consumo * 0.5}')
else:
    print('Sin impuestos')