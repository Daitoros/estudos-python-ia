#Encapsulamento e atributos privados
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #Atributo privado, encapsulamento. Necessário métodos getters/setters
        self.valor = saldo

    def depositar(self, valor):
        self.__saldo = self.__saldo + valor

    def consultar_saldo(self):
        return self.__saldo
conta = ContaBancaria(1100)
print('saldo: ', conta.consultar_saldo())

#print(conta.__saldo) aponta que não há tal atributo

print(conta.valor) #assim é possível acessar o mesmo valor tal como o método consultar_saldo

conta.depositar(100)
print(conta.consultar_saldo())