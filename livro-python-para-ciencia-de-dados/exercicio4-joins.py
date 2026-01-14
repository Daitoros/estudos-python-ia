#executando diferentes joins

import pandas as pd

data = ['Davi', 'Duduka', 'Apolo']
nomes = pd.Series(data, name = 'nomes')
#print(nomes)

data = ['davi.aires', 'duduka.seixas', 'apolo.seixas']
emails = pd.Series(data, name = 'emails')

df = pd.concat([nomes,emails], axis = 1)
# print("\n")
# print(df)

data = ['2555-01','2555-02', '2555-03']
phones = pd.Series(data, name = 'telefones')

df = pd.concat([nomes,emails,phones], axis = 1)
# print("\n")
# print(df)

data = [1000, 2000]
salario = pd.Series(data, name = 'salario')
df_sal = df.join(salario)
print("\n")
print("Left:")
print(df_sal)


#Usado aqui as mesmas variáveis pois é apenas demonstração
data = [1000, 2000, 3000]
salario = pd.Series(data, name = 'salario')
df_sal = df.join(salario)
print("\n")
print("Left 2:")
print(df_sal)
df_sal = df_sal.drop(columns=['salario'])

data = [1000, 2000, 3000, 4000]
salario = pd.Series(data, name = 'salario')
df_sal = df.join(salario, how = 'left')
print("\n")
print("Left 3:")
print(df_sal)
df_sal = df_sal.drop(columns=['salario'])

data = [1000, 2000, 3000, 4000]
salario = pd.Series(data, name = 'salario')
df_sal = df.join(salario, how='right')
print("\n")
print("Right:")
print(df_sal)
df_sal = df_sal.drop(columns=['salario'])

data = [1000, 2000, 3000, 4000]
df_sal = df.join(salario, how='inner')
print("\n")
print("Inner:")
print(df_sal)
df_sal = df_sal.drop(columns=['salario'])

data = [1000, 2000, 3000, 4000]
df_sal = df.join(salario, how='outer')
print("\n")
print("Outer")
print(df_sal)
df_sal = df_sal.drop(columns=['salario'])