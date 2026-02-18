import pandas as pd
# creamos un DataFrame 
data = {
'nombre': ['Ana', 'Luis', 'Maria', 'Pedro', 'Juan'],
'edad': [20, None, 19, 21, None],
'nota': [4.5, 3.8, None, 4.2, 2.5]
}
dataframe = pd.DataFrame(data)
print("-----------------------------")
print(dataframe)
print("-----------------------------")
#funcion para calcular la media de edad y rellenamos edad con la mediana
dataframe['edad'].fillna(dataframe['edad'].median(), inplace=True)
print(dataframe)
print("-----------------------------")
#funcion para calcular la media de nota y rellenamos nota con la mediana
dataframe['nota'].fillna(dataframe['nota'].median(), inplace=True)
print(dataframe)
print("-----------------------------")

