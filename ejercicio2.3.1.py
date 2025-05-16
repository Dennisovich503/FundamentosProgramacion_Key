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