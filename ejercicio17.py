import pandas as pd

# Dataframe del ejercicio 17
data = {
    
    'Employee_ID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E002', 'E006'],
    'Name': ['Ana García', 'Luis Martínez', None, 'Carlos López', 'María Sánchez', 'Luis Martínez', None],
    'Department': ['Sales', 'IT', 'IT', 'HR', 'Sales', 'IT', 'Finance'],
    'Salary': [45000, 52000, None, 38000, 47000, 52000, 42000],
    'Join_Date': ['2020-01-15', '2019-03-20', '2021-05-10', None, '2020-11-30', '2019-03-20', '2022-02-15'],
    'Performance_Score': [8.5, 9.0, 7.5, 8.0, 7.0, 9.0, None]

}

df = pd.DataFrame(data)
# imprimimos el dataframe original
print("-----------------------------")
print(df)
print("-----------------------------")
#vamos a rellenar los usuarios nulos con las palabras "Empleado Desconocido"
df['Name'].fillna('Empleado Desconocido', inplace=True)
#vamos a eliminar tildes y normalizar los nombres de la columna Name, eliminamos espacios en blanco y capitalizamos cada palabra
df['Name'] = df['Name'].str.strip().str.title()
# vamos a eliminar los duplicados basados en la columna Employee_ID, manteniendo el primer registro 
df = df.drop_duplicates(subset='Employee_ID', keep='last')
# vamos a remplazar los salarios nulos con la media de salarios
media_salarios = df['Salary'].mean()
df['Salary'].fillna(media_salarios, inplace=True)
#redondeamos los salarios a 2 decimales para mejor visualización
df['Salary'] = df['Salary'].round(2)
# vamos a rellenar las fechas nulas con la fecha más común en la columna Join_Date
fecha_mas_común = df['Join_Date'].mode()[0]
# rellenamos los valores nulos con fecha_mas_común
df['Join_Date'].fillna(fecha_mas_común, inplace=True)
#creamos la variable media_performance para 
media_performance = df['Performance_Score'].mean()
#rellenar los valores nulos de Performance_Score con la media de Performance_Score
df['Performance_Score'].fillna(media_performance, inplace=True)
# imprimimos el dataframe limpio
print("-----------------------------")
print(df)
print("-----------------------------")

