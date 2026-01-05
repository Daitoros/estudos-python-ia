#Definindo uma Classe/metodo em python com herança e polimorfismo

class Animal:
  def __init__(self, nome, corDoAnimal):
    self.nome = nome
    self.cor = corDoAnimal

class Cachorro(Animal):
  def latir(self):
    return "Au au!"
class Gato(Animal):
  def miar(self):
    return "Miau!"

c = Cachorro("Rex", "Caramelo")
print(c.latir())
print(c.cor, c.nome)