import pandas as pd
# Dataframe del ejercicio 9
data = {
    
'nombre': ['Ana', 'Luis', 'Maria', 'Pedro', 'Juan', 'Laura'],
'nota': [4.8, 3.9, 4.2, 2.7, 3.5, 4.0],
'asistencia': [95, 60, 85, 70, 50, 90]
    
    
}

# creamos un DataFrame con algunos datos de ejemplo
df = pd.DataFrame(data)
print("------------------------------")
print(df)
print("------------------------------")

df['estado'] = df.apply(
    lambda row: 
        'Excelente' if row['nota'] >= 3.5 and row['asistencia'] >= 90
        else 'Bueno' if row['nota'] >= 3.0 and row['asistencia'] >= 80
        else 'Reprobado',
    axis=1
)

