import pandas as pd

# Dataframe del ejercicio 16
data = {
    
    'Order_ID': [101, 102, 103, 104, 105, 106, 107],
    'Customer Name': ['Juan Perez', 'Maria López', None, 'Carlos Ruiz', 'Ana Gómez', 'Luis Fernandez', 'Maria Lopez'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Tablet', 'Laptop', 'mouse'],
    'Price': ['$1,200.50', '25.99', '45.00', '350', '550.75', '$1,200.50', '25.99'],
    'Quantity': [1, 2, 1, 1, 1, 1, 2],
    'Order Date': ['2023-01-15', '2023-01-15', '2023-01-16', '15/01/2023', '2023-01-17', '2023-01-15', '2023-01-15'],
    'City': ['Madrid', 'Barcelona', 'barcelona', 'VALENCIA', 'Sevilla', 'Madrid', 'Barcelona']

}

df = pd.DataFrame(data)
# camos a mostrar solo las 3 primeras filas del dataframe 
print("-----------------------------")
print(df.head(3))
print("-----------------------------")
# vamos a verificar cuantos valores nulos hay en cada columna con el metodo .isnull().sum()
print("Valores nulos por columna:")
print("-----------------------------")
print(df.isnull().sum())
print("-----------------------------")
# ahora solo vamos a contar y mosrar los valores duplicados
print("Valores duplicados por columna:")
print("-----------------------------") 
print(df.duplicated().sum())
print("-----------------------------")
# ahora vamos acontar los valores unicos en cada columna categorica
print("Valores únicos por columna:")
print("-----------------------------")
print("Customer Name:", df['Customer Name'].nunique())
print("Product:", df['Product'].nunique())
print("City:", df['City'].nunique())
print("-----------------------------")





    
