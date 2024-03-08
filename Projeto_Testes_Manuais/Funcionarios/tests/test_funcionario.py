from Funcionarios.funcionario import Funcionario

#Classe de teste não precisa de inicializador (Init)
class TestNome:
    def test_verificar_nome_maisculo(self):
        input = "lucas"
        esperado = "LUCAS"

        funcionario_teste = Funcionario(input, "Ferreira", 28)
        resultado = funcionario_teste.imprimirNomeMaisculo()

        assert resultado == esperado