class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def imprimirNumero1(self):
        return self.numero1

    def imprimirNumero2(self):
        return self.numero2

    def somar(self):
        return self.numero1 + self.numero2

    def subtração(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        return self.numero1 / self.numero2

Conta1 = Calculadora(12,2)
print('O número 1 é igual a {} e o número 2 é igual a {}'.format(Conta1.imprimirNumero1(),Conta1.imprimirNumero2()))
print('A soma dos dois números é igual a', Conta1.somar())
print('A subtração dos dois números é igual a', Conta1.subtração())
print('A multiplicação entre os dois números é igual a ', Conta1.multiplicar())
print('A divisão entre os dois núemros é igual a ', Conta1.dividir())

print('Resumindo: Soma = {} \n Subtração = {} \n Multiplicação = {} \n Divisão = {}'.format(Conta1.somar(), Conta1.subtração(), Conta1.multiplicar(), Conta1.dividir()))
