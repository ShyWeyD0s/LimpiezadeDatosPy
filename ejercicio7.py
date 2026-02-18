import pandas as pd

# Dataframe del ejercicio 6
data = data = {
'nombre': ['Ana', 'Luis', 'Maria', 'Pedro'],
'nota': [4.5, 3.8, 4.0, 2.9]
}
# creamos un DataFrame con algunos datos de ejemplo
df = pd.DataFrame(data)
#imprimimos el DataFrame original
print("------------------------------")
print(df)
print("------------------------------")
# vamos a insertar una columna llamada estado que indique para guardar el estado del estudiante si es aprobado o reprobado dependiendo de la nota
# hacemos esto con la función apply y una función lambda que compruebe si la nota es mayor o igual a 4.0 para aprobar o menor a 4.0 para reprobar
df['estado'] = df['nota'].apply(lambda comprobarEstado: 'aprobado' if comprobarEstado >= 4.0 else 'reprobado')
print("------------------------------")
print(df)
print("------------------------------")