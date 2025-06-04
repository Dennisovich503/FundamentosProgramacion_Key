

'''
Clase:        Clase 1
Tema:         Uso de variables, entradas y salidas
Ejercicio:    1.3.2
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-14
Estado:       Terminado 
'''

nombre = input("Ingrese su nombre: ")

correo = f"{nombre.lower()}@keyinstitute.edu.sv"

print(f"\nCorreo generado: {correo}")
