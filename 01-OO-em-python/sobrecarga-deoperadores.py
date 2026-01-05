#sobrecarga de operadores
# Como sempre, o começo, "__init__", "__add__", "__str__" é identificando o retorno!


class Vetor: 
    def __init__(self, x, y):           #Construtor/iniciação do vetor
        self.x = x
        self.y = y
    def __add__(self, other):           #Aqui é o método para soma
        return Vetor(self.x + other.x, self.y + other.y)
    def __str__(self):                  #Aqui é pra exibição dos nomes. Sem esse não exibe corretamente os strings. É um "getter de strings"
        return f'({self.x}, {self.y})'  #O f é para concatenar

v1 = Vetor(2, 3)
v2 = Vetor(1,5)
v3 = v1 + v2

print('v1: ', v1)
print('v2: ', v2)
print('v3: ', v3)
