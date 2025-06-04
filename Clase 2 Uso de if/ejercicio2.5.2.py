'''
Clase:        Clase 2
Tema:         Uso de if
Ejercicio:    2.3.1
Descripción:  Eres parte del equipo de desarrollo de un sistema de defensa automatizado para una
base científica ubicada en una zona volcánica peligrosa. Por cuestiones de seguridad, el
sistema debe identificar si un objeto detectado por sensores (un punto con
coordenadas (x, y)) se encuentra en una zona peligrosa, de manera que pueda activarse
una alerta inmediata. Las zonas de peligro están definidas como:
• Zona de peligro 1: el punto se encuentra en el primer cuadrante, es decir, x > 0 y y > 0.
• Zona de peligro 2: el punto está dentro de un círculo de radio 5 centrado en el origen
(0, 0), es decir, x² + y² <= 25

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-06-16
Estado:       Terminado 
'''

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
