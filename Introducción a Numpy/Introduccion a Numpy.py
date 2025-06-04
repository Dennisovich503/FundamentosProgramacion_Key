import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])


#-------------------DESARROLLO DE LA GUÍA---------------
# Exploración inicial de los datos
print( "Dimensiones:", consumo.ndim)
print( "Forma:",consumo. shape)
print( "Tipo de datos:", consumo.dtype)
print( "Consumo primer hogar:", consumo[0])
print( "Consumo el miércoles (día 3):", consumo[:, 2])


# Promedto de consumo por hogar
promedio_por_hogar = np.mean( consumo, axis=1)
# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean( consumo, axis=0)
# Suma total de consumo en la semana de los 10 hogares
total_consumo = np. sum( consumo)
print( promedio_por_hogar)
print( promedio_por_dia)
print( total_consumo)



#Máximo por hogar
maximos = np.max(consumo, axis=1)
# Minimo por día
minimos = np.min(consumo, axis=0)
# Desviación estándar global
desviacion = np.std( consumo)
print(maximos)
print(minimos)
print(desviacion)


# Suma por hogar (semana)
consumo_total_hogar = np.sum( consumo, axis=1)
# Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Indice del hogar con mejor
consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)
print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)

# Suma por hogar (semana)
consumo_total_hogar = np.sum( consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")
# Compara cada hogar con un valor mayor a 108
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos) [0]
print(f'ids de hogares con consumo mayor a 160: {consumo_mayor_100}')

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo-max() - consumo.min( ))
# Resultado
print(consumo_normalizado)



#---------------------------------DESARROLLO DEL CUESTIONARIO------------
# 1. Consumo del hogar 5 el viernes (día 5, índice 4)
print(f'El consumo del hogar 5 el viernes es: {consumo[4, 4]}')

# 2. Consumo de los últimos 3 hogares el domingo (columna 6)
print(f'El consumo de los últimos 3 hogares el domingo: {consumo[-3:, 6]}')

# 3. Promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6)
fs = consumo[:, [5, 6]]
p_fs = np.mean(fs)
print(f'El promedio de consumo durante los fines de semana es: {p_fs}')

# 4. Día de la semana con mayor desviación estándar entre hogares
desv_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion = np.argmax(desv_por_dia)
print(f'El día con mayor desviación estándar es el día {dia_mayor_desviacion} con un valor de {desv_por_dia[dia_mayor_desviacion]:.2f}')
print('Esto indica que ese día hay mayor variabilidad en el consumo entre los hogares.')

# 5. Tres hogares con menor consumo total durante la semana
suma = np.sum(consumo, axis=1)
i_menor_consumo = np.argsort(suma)[:3] 
valores_menor_consumo = suma[i_menor_consumo]
print('Los 3 hogares con menor consumo total son:')
for i in range(len(i_menor_consumo)):
    hogar = i_menor_consumo[i]
    total = valores_menor_consumo[i]
    print(f' - Hogar {hogar} con un total de {total:.2f}')


# 6. Nuevo consumo total semanal del hogar 3 si aumenta un 10% cada día
hogar_3 = consumo[2]
hogar_3_incrementado = hogar_3 * 1.10
nuevo_total_hogar_3 = np.sum(hogar_3_incrementado)
print(f'El nuevo consumo total del hogar 3 con un aumento del 10% diario sería: {nuevo_total_hogar_3}')