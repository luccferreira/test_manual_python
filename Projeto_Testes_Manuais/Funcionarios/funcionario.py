
class Funcionario:
    def __init__(self, nome, sobrenome,idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def imprimirNomeMaisculo(self):
        return self.nome.upper()


