#Os construtores instanciam e os destrutores destroem o arquivo ao final da execução do código.

class Pessoa:
    def __init__ (self, nome):
        self.nome = nome
        print(self.nome, "foi criado")

    def __del__(self):
        print(self.nome, 'foi destruido')

p1 = Pessoa( 'Davi')
p2 = Pessoa('AE')

print('-----------------------------------')