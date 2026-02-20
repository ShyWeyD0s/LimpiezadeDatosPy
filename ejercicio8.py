import pandas as pd 
import numpy as np

# creamos un DataFrame con los datos del ejercicio 8
data = {
    
    'id': [1, 2, 3, 3, 4, 5],
    'nombre': ['Ana', 'Luis', None, 'Maria', 'Pedro', 'Juan'],
    'edad': [20, None, 150, 19, 21, 200],
    'nota': [4.5, 3.8, None, 4.0, None, 2.5],
    'ciudad': ['cali ', 'POPAYAN', None, 'Cali ', ' popayan', 'Medellin']
}
# Imprimimos el dataframe original

df = pd.DataFrame(data)

condiciones = [
    df['nota'] < 3.5,
]
opciones = [
    'Reprobado'
]
default_value = 'Aprobado'

print("-----------------------------")
print(df)
print("-----------------------------")
# Eliminamos lso duplicados basados en la columna id, manteniendo el último registro
df = df.drop_duplicates(subset='id', keep='last')
# vamos a normalizar la columna ciudad, eliminando espacios en blanco y capitalizando
df['ciudad'] = df['ciudad'].str.strip().str.title()
# vamos a rellenar los valores faltantes en la columna edad con la mediana antes de corregir inconsistencias
median_age = df['edad'].median()
df['edad'].fillna(median_age, inplace=True)
# vamos a corregir las edades inconsistentes, reemplazándolas por la mediana de la columna edad
df.loc[df['edad'] > 100, 'edad'] = median_age
# vamos a rellenar con 0.0 los valores faltantes en la columna nota
df['nota'].fillna(0.0, inplace=True)
print("-----------------------------")
print(df)
print("-----------------------------")
# ahora vamos a crear una columna llamada ´estado´ que indique si aprobo o reprobo dependiendo de la nota, usando una función lambda
df['estado'] = np.select(condiciones, opciones, default=default_value)
# imprimimos el dataframe final
print("-----------------------------")  
print(df)
print("-----------------------------")
