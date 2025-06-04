

'''
Clase:        Clase 1
Tema:         Uso de listas
Ejercicio:    1.3.1
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar

Autor:        Dennis Alejandro Palacios López
Fecha:        2025-05-14
Estado:       Terminado 
'''


total = float(input("Ingrese el total de la cuenta: $"))


porcentaje = float(input("Ingrese el porcentaje de propina (por ejemplo, 10 para 10%): "))


propina = total * (porcentaje / 100)
total_con_propina = total + propina

print()
print(f"Total de la cuenta: ${total:.2f}")
print(f"Propina: ${propina:.2f}")
print(f"Total de la cuenta con propina ({int(porcentaje)}%): ${total_con_propina:.2f}")

