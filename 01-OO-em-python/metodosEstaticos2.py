class Aluno:
    total_alunos = 0

    def __init__(self, nome):
        self.nome = nome
        Aluno.total_alunos += 1

    @classmethod  #classe estática que não depende de um objeto, pertencendo à classe aluno
    def total(cls):
        return cls.total_alunos

a1 = Aluno('João')
a2 = Aluno('Pedro')

print('TotalAlunos: ', Aluno.total())