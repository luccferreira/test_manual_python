
from Estacionamento.veiculos import Veiculo

class Motos(Veiculo):
    def __init__(self, modelo, marca, tipo):
        super().__init__(modelo,marca)
        self.tipo = tipo

    def __str__(self):
        return 'A marca da moto é {} do modelo {} e é {}'.format(self.modelo,self.marca,self.tipo)