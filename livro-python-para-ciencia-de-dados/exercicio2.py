import numpy as np

jeff_salary = [2700,3000,3000]
nick_salary = [2600,2800,2800]
tom_salary = [2300,2500,2500]

base_salary =  np.array([jeff_salary, nick_salary, tom_salary])

jeff_bonus = [500,400,400]
nick_bonus = [600,300,400]
tom_bonus = [200,500,400]

bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])

salary_bonus = base_salary + bonus

print("\nSalário Base:\n")
print(base_salary)
print("\n")
print("Bônus:\n")
print(bonus) 
print("\n")
print("Salário Total:")
print(salary_bonus)
                                                                #Aqui é como uma verdadeira matriz: eixo 0 representa 
maiorSalFunc = np.amax(salary_bonus, axis = 1)                  #(axis = 1) Percorre e compara por linha (cada funcionario está em uma linha). no final vai ter um total de valores equivalente ao total de linhas
maiorSalmes = np.amax(salary_bonus, axis = 0)                   #(axis = 0) Percorre e compara por coluna (os meses estão representados por colunas). no final vai ter um total de valores equivalente ao total de colunas

#conjuntoMaior = np.concatenate((maiorSal3mes, maiorSalCol))            não é necessário concatenar aqui
#maiorSal = np.amax(conjuntoMaior, axis=1)

maiorSal = np.amax(salary_bonus)                                        #Encontrando o maior valor de todos
medianaSal = np.median(salary_bonus)                 
mediaSal= np.average(salary_bonus)
print("\n")
print(maiorSal)
print(medianaSal)
print(mediaSal)

print("\n Maiores salários dos últimos 3 meses:")
print(maiorSalmes)
print("\n Média maiores salários dos últimos 3 meses")
mediaMaioresSal = np.average(maiorSalmes)
print(mediaMaioresSal)