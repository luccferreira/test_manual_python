
from Estacionamento.veiculos import Veiculo

class Carros(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        return 'O modelo do carro é {}, sendo da marca {} e possui {} portas'.format(self.marca,self.modelo,self.portas)
