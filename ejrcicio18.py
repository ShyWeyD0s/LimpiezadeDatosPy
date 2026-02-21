import pandas as pd
import numpy as np

# Dataframe del ejercicio 18

data = {
    
    'Product_ID': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'Product_Name': ['laptop gaming', 'MOUSE INALAMBRICO', 'Teclado Mecánico', 'monitor 4k', 'AURICULARES GAMER', 'silla ergonómica'],
    'Category': ['Electrónica', 'Accesorio', 'Electrónica', 'electrónica', 'accesorio', 'Mobiliario'],
    'Price_USD': [1200.50, 45.99, 89.99, 350.00, 129.99, 299.99],
    'Weight_g': [2500, 150, 800, 5500, 350, 12500],
    'Stock': [15, 120, 45, 28, 67, 12],
    'Rating': ['4.5/5', '3.8/5', '4.2/5', '4.7/5', '4.0/5', '4.9/5']

}

df = pd.DataFrame(data)

#imprimir el DataFrame original
print("-------------Dataframe Original-----------------")
print(df)
print("------------------------------")

#limpieza y manejo de datos

# vamos a normalizar la informacion de la colm Product_Name
df['Product_Name'] = df['Product_Name'].str.strip().str.title()
# vamos a normalizar la informacion de la colm Category, tambien eliminamos acentos y caracteres especiales, y normalizamos a mayusculas
df['Category'] = df['Category'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.strip().str.capitalize()
print(df) 
# Vamos a convertir los dolares a euros y añadir estos valores a la nueva columna
precio_euros = df['Price_USD'] * 0.85
df['Price_EUR'] = precio_euros.round(2)
# convertimos el peso degramos a kilos
peso_kilos = df['Weight_g'] / 1000
# lo redondeamos a tres decimales 
df['Weight_kg'] = peso_kilos.round(3)
#convertimos la columna de Rating a valores flotantes, eliminando el texto "/5" y convirtiendo a float
#usamos str.replace para eliminar el texto "/5" y luego astype(float) para convertir a float
rating_float = df['Rating'].str.replace('/5', '').astype(float)
df['Rating'] = rating_float

df['Stock_Status'] = np.select(
    # codiciones
    [
        df['Stock'] > 50,
        df['Stock'] >= 20
    ],
    # estados
    ['Alto', 'Medio'],
    default='Bajo'
)

# imprimimos el dataframe final con las nuevas columnas y la informacion ya limpia y normalizada
print("------------Dataframe Final-----------------")
print(df)
print("---------------------------------------------")
print(":'3")


