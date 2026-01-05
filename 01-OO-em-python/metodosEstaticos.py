#Metodos estaticos não precisam de instâncias (não precisam de construtores )

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
calc = Calculadora()

print('soma: ', calc.somar(2,3), '\n subtração:', calc.subtrair(2,3))

