
class Carros:
    def __init__(self, marca, modelo, ano, cor, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def imprimirMarca(self):
        return self.marca

    def imprimirModelo(self):
        return self.modelo

    def imprimirAno(self):
        return self.ano

    def imprmirCor(self):
        return self.cor

    def imprimirQuilometragem(self):
        return self.quilometragem

Carro1= Carros("Chevrolet", "Celta", 2006, "Cinza", 20000.0)
print('A marca do carro é {} \n O modelo do carro é {} \n O ano do carro é {} \n A cor do carro é {} \n A quilometragem do carro é {}'.format(Carro1.imprimirMarca(), Carro1.imprimirModelo(), Carro1.imprimirAno(), Carro1.imprmirCor(), Carro1.imprimirQuilometragem()))


