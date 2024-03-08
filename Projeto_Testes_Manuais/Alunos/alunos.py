
class Alunos:
#Inicializador/construtor de uma classe, o que há dentro do objeto, os atributos dos Alunos
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
#Self: voltado sempre ao objeto que criei
    def imprimirNome(self):
        return self.nome

    def imprimirNota1(self):
        return self.nota1

    def imprimirNota2(self):
        return self.nota2

#Retornar uma apresentação string de um objeto
    def __str__(self):
        return self.nome

#Inicializar o objeto
AlunoRenato = Alunos("Renato", 8, 9)
print(AlunoRenato)
print(AlunoRenato.imprimirNota1())
print(AlunoRenato.imprimirNota2())

#print(AlunoRenato.imprimirNome())