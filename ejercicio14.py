import pandas as pd
import numpy as np

# Dataframe del ejercicio 13
data = {
    
    'id': [1,2,3,3,4,5,6],
    'nombre': ['Ana','Luis',None,'Maria','Pedro','Juan','Laura'],
    'edad': [20,22,None,19,150,-3,21],
    'nota': [4.5,3.8,None,4.0,None,2.5,4.7],
    'ciudad': ['cali ','POPAYAN',None,'Cali ',' popayan','medellin','CALI']

}

df = pd.DataFrame(data)
print("-----------------------------")
print(df)
print("-----------------------------")
# ahora empezamos con la limpieza de datos 
# eliminamos duplicados por id 
df = df.drop_duplicates(subset = 'id', keep = 'last')
# ahora tratamos todos los valores de edades irreales
df.loc[df['edad'] > 100, 'edad'] = np.nan
df.loc[df['edad'] < 0, 'edad'] = np.nan
# ahora los valoes nuelos de edad los llenamos con la mediana 
median_age = df['edad'].median()
df['edad'] = df['edad'].fillna(median_age)
# ahora tratamos los valores nulos de nota, los llenamos con la mediana de nota
# primero creamos la variable de la mediana de nota
# metodo .median() para calcular la mediana de la columna nota
median_nota = df['nota'].median()
# ahora llenamos los valores nulos de nota con la mediana de nota
# metodo .fillna()
df['nota'] = df['nota'].fillna(median_nota)
# normalizamos y capitalizamos la columna ciudad, eliminamos espacios en blanco y capitalizamos
df['ciudad'] = df['ciudad'].str.strip().str.title()
# imprimimos el dataframe ya limpio y normalizado
print("-----------------------------")
print(df)
print("-----------------------------")
# vamos a crear columna de estado para aprobado o reprobado
# vamos a usar la función np.select para crear la columna de estado, con condiciones para aprobado o reprobado
df['estado'] = np.select(
    [
        df['nota'] >= 3.0,
        df['nota'] < 3.0
    ],
    ['Aprobado', 'Reprobado'],
    default='Reprobado'
)

# imprimimos el dataframe final con la columna de estado
print("-----------------------------")
print(df)
print("-----------------------------")