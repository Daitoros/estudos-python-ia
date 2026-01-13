#Criando uma Series e dataframes

import pandas as pd

data = ['Davi', 'Duduka', 'Apolo']
nomes = pd.Series(data, name = 'nomes')
print(nomes)

data = ['davi.aires', 'duduka.seixas', 'apolo.seixas']
emails = pd.Series(data, name = 'emails')

df = pd.concat([nomes,emails], axis = 1)
print("\n")
print(df)