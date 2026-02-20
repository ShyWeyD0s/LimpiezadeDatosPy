import pandas as pd
import numpy as np
# Dataframe del ejercicio 11

data = {
'cliente': ['A', 'B', 'C', 'D', 'E', 'F'],
'total_compras': [120000, 450000, 800000, 250000, 600000, 300000]
}

df = pd.DataFrame(data)

condiciones = [
    (df['total_compras'] >= 700000),
    (df['total_compras'] >= 400000),
    (df['total_compras'] >= 200000)
]
# Definimos los resultados para cada condición
opciones = ['Premium', 'Oro', 'Plata']
# El último argumento es el valor por defecto (Bronce)
df['segmento'] = np.select(condiciones, opciones, default='Bronce')
print("-----------------------------")
print(df)
print("-----------------------------")