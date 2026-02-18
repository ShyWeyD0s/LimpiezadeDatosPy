import pandas as pd
import numpy as np
# creamos un DataFrame con algunos datos de ejemplo
data = {
'ID': [1, 2, 3, 4],
'Nombre': [' juan ', 'ANNA', 'Luis', 'Marta'],
'Edad': [25, np.nan, -5, 30],
'Ciudad': ['Madrid', 'Bogota', 'Mexico', None]
}
# creamos el DataFrame y limpiamos los datos
dataframe = pd.DataFrame(data)
dataframe['Nombre'] = dataframe['Nombre'].str.strip().str.title()
dataframe['Edad'] = dataframe['Edad'].fillna(dataframe['Edad'].mean())
dataframe['Ciudad'] = dataframe['Ciudad'].fillna('Desconocida')
print(dataframe)


# sintaxis general df.loc[filas, columnas]
# .loc es un método de selección y filtrado de datos
# basado en etiquetas
# -----------------------------
# mostramos la columna 'Edad'
dataframe.loc[:, 'Edad']
# mostramos las filas donde la edad es mayor a 20
dataframe.loc[dataframe['Edad'] > 20, 'Edad']

